import modal
import subprocess

qwen_image = (
    modal.Image.debian_slim()
    .apt_install("git")
    .apt_install("nano")
    .pip_install("comfy-cli")
    .run_commands(
        "comfy --skip-prompt install --nvidia",
    )
    .run_commands(
        # Qwen Image 2512 Models
        # Text Encoders
        "comfy --skip-prompt model download --url https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors --relative-path models/text_encoders",
        # LoRAs
        "comfy --skip-prompt model download --url https://huggingface.co/lightx2v/Qwen-Image-Lightning/resolve/main/Qwen-Image-Lightning-4steps-V1.0.safetensors --relative-path models/loras",
        # Diffusion Models
        "comfy --skip-prompt model download --url https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/diffusion_models/qwen_image_2512_fp8_e4m3fn.safetensors --relative-path models/diffusion_models",
        "comfy --skip-prompt model download --url https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/diffusion_models/qwen_image_2512_bf16.safetensors --relative-path models/diffusion_models",
        # VAE
        "comfy --skip-prompt model download --url https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/vae/qwen_image_vae.safetensors --relative-path models/vae",
        
        # Z-Image Turbo Models
        # Text Encoders
        "comfy --skip-prompt model download --url https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/text_encoders/qwen_3_4b.safetensors --relative-path models/text_encoders",
        # Diffusion Models
        "comfy --skip-prompt model download --url https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/diffusion_models/z_image_turbo_bf16.safetensors --relative-path models/diffusion_models",
        # VAE
        "comfy --skip-prompt model download --url https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/vae/ae.safetensors --relative-path models/vae",
        # ControlNet Model (for advanced workflows)
        "comfy --skip-prompt model download --url https://huggingface.co/alibaba-pai/Z-Image-Turbo-Fun-Controlnet-Union/resolve/main/Z-Image-Turbo-Fun-Controlnet-Union.safetensors --relative-path models/model_patches",
        # Pixel Art LoRA for Z-Image Turbo
        "comfy --skip-prompt model download --url https://huggingface.co/tarn59/pixel_art_style_lora_z_image_turbo/resolve/main/pixel_art_style_z_image_turbo.safetensors --relative-path models/loras",
    )
)

app = modal.App(name="qwen-image-2512-comfyui", image=qwen_image)

@app.function(
    max_containers=1,
    scaledown_window=300,
    timeout=3200,
    gpu="A100-40GB",
)
@modal.concurrent(max_inputs=10)
@modal.web_server(8000, startup_timeout=60)
def ui():
    subprocess.Popen("comfy launch -- --listen 0.0.0.0 --port 8000", shell=True)
