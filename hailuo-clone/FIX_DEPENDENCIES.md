# 🔧 Fix Dependency Issues

If you're seeing the transformers error, follow these steps:

## Quick Fix

Run these commands in order:

```bash
# 1. Uninstall conflicting packages
pip uninstall -y transformers diffusers

# 2. Install compatible versions
pip install transformers==4.44.2
pip install diffusers==0.30.3
pip install sentencepiece
pip install protobuf

# 3. Restart the backend
python backend_local.py
```

## Full Clean Install

If the quick fix doesn't work, do a complete reinstall:

```bash
# 1. Create a fresh virtual environment
python3 -m venv venv_clean
source venv_clean/bin/activate  # On Windows: venv_clean\Scripts\activate

# 2. Install PyTorch first (GPU version)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# Or for CPU only:
# pip install torch torchvision torchaudio

# 3. Install all requirements
pip install -r requirements_local.txt

# 4. Run the backend
python backend_local.py
```

## What Was the Problem?

The error occurred because:
- **Old transformers version** didn't have the correct T5 tokenizer loading methods
- **Missing sentencepiece** library (required for T5 tokenizer)
- **Incompatible diffusers version** with the transformers library

## Verified Working Versions

These versions are tested and working:
- `transformers>=4.44.0`
- `diffusers>=0.30.0`
- `sentencepiece>=0.1.99`
- `protobuf>=3.20.0`

## Still Having Issues?

Try this diagnostic:

```python
# Test if transformers is working
python -c "from transformers import T5Tokenizer; print('✅ Transformers OK')"

# Test if diffusers is working
python -c "from diffusers import CogVideoXPipeline; print('✅ Diffusers OK')"
```

If either fails, reinstall that specific package:
```bash
pip install --upgrade --force-reinstall transformers
pip install --upgrade --force-reinstall diffusers
```

---

**After fixing, restart the backend and it should work! 🎉**
