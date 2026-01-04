# ComfyUI Qwen Image 2512 + Z-Image Turbo on Modal

A clean, minimal Modal script to run ComfyUI with **both** Qwen Image 2512 and Z-Image Turbo models for high-quality image generation and testing.

## Features

- **One-click deployment**: Simple `modal serve` command
- **Dual model support**: Qwen Image 2512 + Z-Image Turbo
- **All models included**: Text encoders, diffusion models, VAEs, LoRAs, and ControlNet
- **A100 GPU**: Optimized for both model performances
- **Web interface**: Full ComfyUI UI accessible via browser
- **Persistent storage**: Models cached for reuse

## Quick Start

### 1. Install Dependencies
```bash
# Clone the repository
git clone https://github.com/innovativebran/qwen-image-2512-modal.git
cd qwen-image-2512-modal

# Install Python dependencies
pip install -r requirements.txt

# Alternative: Install modal directly
pip install modal>=1.2.0
```

### 2. Authenticate with Modal
```bash
modal setup
```

### 3. Deploy the App
```bash
modal serve qwen.py
```

### 4. Access ComfyUI
The command will output a URL like:
```
https://your-app-id--your-workspace.modal.app
```

Open this URL in your browser to access the ComfyUI interface.

## Usage Tutorial

### Qwen Image 2512

1. **Open the ComfyUI URL** provided after deployment
2. **Load the Qwen Image 2512 workflow** (models are pre-loaded)
3. **Enter your prompt** in the text box
4. **Click "Queue Prompt"** to generate

### Z-Image Turbo

1. **Open the ComfyUI URL** provided after deployment
2. **Load the Z-Image Turbo workflow** or create a new one
3. **Select Z-Image Turbo models** from the dropdown menus
4. **Add the pixel art LoRA** for pixel art style (optional)
5. **Enter your prompt** and adjust settings
6. **Click "Queue Prompt"** to generate

#### Pixel Art Style with LoRA
- Load the `pixel_art_style_z_image_turbo.safetensors` LoRA
- Use prompts like: "pixel art character, 8-bit style, gaming character"
- Great for: Game sprites, retro art, pixel animations

### Recommended Settings

#### Qwen Image 2512
- **Resolution**: 1328x1328 (default)
- **Steps**: 4 (Lightning mode - fast)
- **CFG Scale**: 7.0
- **Sampler**: Euler
- **Scheduler**: Simple

#### Z-Image Turbo
- **Resolution**: 1024x1024 (default)
- **Steps**: 4-9 (Turbo mode - very fast)
- **CFG Scale**: 7.0
- **Sampler**: Euler
- **Scheduler**: Simple

### Example Prompts

#### General Prompts
```
A beautiful landscape with mountains and lakes
A detailed portrait of a woman
A cyberpunk city at night
A fantasy castle in the clouds
Photorealistic image of a modern office
```

#### Pixel Art Style (with Z-Image Turbo LoRA)
```
Pixel art character, 8-bit style, gaming character
Retro game sprite, 16-bit pixel art
Pixel art landscape, cute style
8-bit warrior character, game design
Pixel art castle, fantasy game style
```

## Models Included

### Qwen Image 2512 Models

#### Text Encoders
- `qwen_2.5_vl_7b_fp8_scaled.safetensors` - Main text encoder

#### Diffusion Models
- `qwen_image_2512_fp8_e4m3fn.safetensors` - Fast FP8 model (default)
- `qwen_image_2512_bf16.safetensors` - High-quality BF16 model (use if you have enough VRAM)

#### VAE
- `qwen_image_vae.safetensors` - Image decoder

#### LoRAs
- `Qwen-Image-Lightning-4steps-V1.0.safetensors` - Lightning LoRA for fast 4-step generation

### Z-Image Turbo Models

#### Text Encoders
- `qwen_3_4b.safetensors` - Z-Image Turbo text encoder

#### Diffusion Models
- `z_image_turbo_bf16.safetensors` - Z-Image Turbo diffusion model

#### VAE
- `ae.safetensors` - Z-Image Turbo VAE

#### ControlNet (Advanced)
- `Z-Image-Turbo-Fun-Controlnet-Union.safetensors` - Fun Union ControlNet for guided generation

#### LoRAs
- `pixel_art_style_z_image_turbo.safetensors` - Pixel art style LoRA for Z-Image Turbo

## File Structure

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 text_encoders/
│   │      ├── qwen_2.5_vl_7b_fp8_scaled.safetensors (Qwen Image 2512)
│   │      └── qwen_3_4b.safetensors (Z-Image Turbo)
│   ├── 📂 loras/
│   │      ├── Qwen-Image-Lightning-4steps-V1.0.safetensors (Qwen Image 2512)
│   │      └── pixel_art_style_z_image_turbo.safetensors (Z-Image Turbo)
│   ├── 📂 diffusion_models/
│   │      ├── qwen_image_2512_bf16.safetensors (Qwen Image 2512)
│   │      ├── qwen_image_2512_fp8_e4m3fn.safetensors (Qwen Image 2512)
│   │      └── z_image_turbo_bf16.safetensors (Z-Image Turbo)
│   ├── 📂 vae/
│   │      ├── qwen_image_vae.safetensors (Qwen Image 2512)
│   │      └── ae.safetensors (Z-Image Turbo)
│   └── 📂 model_patches/
│          └── Z-Image-Turbo-Fun-Controlnet-Union.safetensors (Z-Image Turbo)
```

## Performance Tips

### Qwen Image 2512
1. **Use the FP8 model** for faster generation (default)
2. **4 steps** is usually sufficient for good quality with Lightning LoRA

### Z-Image Turbo
1. **4-9 steps** provides excellent quality (Turbo mode)
2. **Very fast inference** - optimized for speed
3. **Great for photorealistic images**

### General
1. **A100-40GB** GPU provides optimal performance for both models
2. **Batch multiple generations** for efficiency
3. **Z-Image Turbo** is generally faster than Qwen Image 2512

## Troubleshooting

### Installation Issues

**If you get "modal-client is no longer being updated" error:**
```bash
pip uninstall modal-client -y
pip install modal>=1.2.0
```

**If modal command doesn't work:**
```bash
# Try using python module
python -m modal serve qwen.py

# Or reinstall specific version
pip uninstall modal -y
pip install modal==1.2.0
```

### If the URL doesn't work:
1. Wait 2-3 minutes for full startup
2. Check the Modal dashboard for app status
3. Try refreshing the URL

### If generation fails:
1. Ensure all models downloaded successfully
2. Check the ComfyUI console for errors
3. Try a simpler prompt first

### Performance issues:
1. Use the FP8 model instead of BF16
2. Reduce image resolution
3. Use fewer steps (4 is usually enough)

## Requirements

- **Python 3.8+**
- **Modal account** (free tier available)
- **A100-40GB GPU access** (may require billing)
- **~30GB storage** for models (both Qwen Image 2512 + Z-Image Turbo)

### Python Dependencies
See `requirements.txt` for the complete list:
```bash
modal>=1.2.0
```

## Configuration

You can modify these settings in `qwen.py`:

- **GPU**: Change `gpu="A100-40GB"` to other available GPUs
- **Timeout**: Adjust `timeout=3200` for longer/shorter sessions
- **Container lifetime**: Modify `scaledown_window=300`

## License

This script uses Qwen Image 2512 and Z-Image Turbo models. Please check the model licenses on Hugging Face for usage terms.

- **Qwen Image 2512**: https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI
- **Z-Image Turbo**: https://huggingface.co/Comfy-Org/z_image_turbo
