import os
from fal_client import subscribe

# 设置你的 API KEY
os.environ["FAL_KEY"] = "44b7cef0-30e6-49b8-80fd-1e1575b644bc:f59fd38819ae69bb48f3c11a6eaa2b1"

# Prompt
prompt = """
cute chibi pet avatar,
3d cartoon style,
pixar style,
adorable,
big sparkling eyes,
soft fur,
toy texture,
premium quality,
octane render,
cinematic lighting
"""

# 调用 Flux Schnell 图像生成
result = subscribe(
    "fal-ai/flux/dev/image-to-image",
    arguments={
        "prompt": prompt,
        "image_url": "https://fal.media/files/panda/example.png",
        "strength": 0.7,
        "num_inference_steps": 28,
        "guidance_scale": 3.5
    }
)

print("生成完成：")
print(result)