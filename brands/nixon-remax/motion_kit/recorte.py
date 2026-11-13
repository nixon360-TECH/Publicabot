from rembg import remove, new_session
from PIL import Image
s=new_session("u2net_human_seg")
im=Image.open(r"E:\Lotificación Alvarez\_marca\03_personas\1000125792 (1).png").convert("RGB")
out=remove(im,session=s,alpha_matting=True,alpha_matting_foreground_threshold=240,alpha_matting_background_threshold=10,alpha_matting_erode_size=8)
out.save(r"E:\NIXON360_CONTENTOPS\04_PROJECTS_EDITABLE\N360-20261112-0001\assets\nixon_recorte.png"); print("ok",out.size)
