import aiohttp
import asyncio
import rich
import os
import aiofiles
from data import data
from rich.console import Console
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from convert_to_pdf import convert_html_to_pdf

console = Console()
async def get_data(url, session, sem, filename):
    
    os.makedirs("lectures", exist_ok=True)
    
    async with sem: 
        async with session.get(url) as response:
           if(response.status == 200):
               content = await response.text(errors='replace')
               
               path = os.path.join("lectures", filename)
               encoding = response.get_encoding()
               async with aiofiles.open(path, mode='w', encoding='utf-8',errors=encoding) as f :
                   await f.write(content)
               rich.print("[green] download successful!! [/green]")
               return content
           else:
               rich.print(f"[red] download failed {url}, status = {response.status}[/red]")


async def main():
    obj = data()
    urls = obj.send_data()
    sem = asyncio.Semaphore(5)
    async with aiohttp.ClientSession() as session:
        # base_url = "https://www.cse.iitk.ac.in/users/dheeraj/cs425/"
        urls = [link for link in urls] # base_url + link.replace("./", "") 
        file_names = [f"lec{i:02}.html" for i in range(1, len(urls) + 1)]
        tasks = [get_data(url, session, sem, filename=filename) for url, filename in zip(urls, file_names)]
        result = await asyncio.gather(*tasks)
        os.makedirs("images", exist_ok=True)
        for html, url in zip(result,urls):
            if html:
                soup = BeautifulSoup(html, 'html.parser')
                images = soup.find_all('img')
                
                for img in images:
                    img_src = img.get('src')
                    if img_src:
                        full_img_url = urljoin(url, img_src)
                        try:
                            async with session.get(full_img_url) as img_resp:
                                if img_resp.status == 200:
                                    img_data = await img_resp.read()
                                    img_name = os.path.basename(img_src)
                                    save_path = os.path.join("images", img_name)
                                    with open(os.path.join("images", img_name), 'wb') as f:
                                        f.write(img_data)
                                        rich.print(f"[blue] Saved image: {img_name} [/blue]")
                        except Exception as e:
                            rich.print(f"[red] Could not download {full_img_url}: {e} [/red]")
                
                
                
            
        
        
if __name__ == '__main__':
    asyncio.run(main())
    try:
        convert_html_to_pdf('lectures', 'files.pdf')
        rich.print("[bold green]PDF Conversion Complete![/bold green]")
    except Exception as e:
        rich.print(f"[bold red]PDF Conversion Failed: {e}[/bold red]")
        

