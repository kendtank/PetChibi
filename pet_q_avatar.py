import os
from fal_client import subscribe

# 设置你的 API KEY
os.environ["FAL_KEY"] = "44b7cef0-30e6-49b8-80fd-1e1575b644bc:f59fd38819ae69bb48f3c11a6eaa2b1"

# Prompt
prompt = """
cute chibi maine coon cat,
orange and white fur,
fluffy long hair,
big sparkling eyes,
adorable expression,
3d pixar style,
premium vinyl toy texture,
soft fur details,
cinematic lighting,
octane render,
kawaii style,
high detail,
cute little paws,
center composition,
soft shadows,
collectible figure style
"""

# 调用 Flux Schnell 图像生成
result = subscribe(
    "fal-ai/flux/dev/image-to-image",
    arguments={
        "prompt": prompt,
        "image_url": "https://github.com/kendtank/PetChibi/blob/main/daoba_cat.jpg",
        "strength": 0.7,
        "num_inference_steps": 28,
        "guidance_scale": 3.5
    }
)

print("生成完成：")
print(result)
