#!/usr/bin/env python3
"""
FFmpeg Video to GIF Converter
Because sometimes you need that perfect reaction GIF 🎬➡️🎞️
"""

import argparse
import subprocess
import sys
import os
from pathlib import Path

def run_command(cmd, description):
    """Run a command and handle errors like a boss"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed!")
        print(f"Command: {cmd}")
        if e.stderr:
            print(f"Error: {e.stderr}")
        return False

def compress_video(input_file, output_file, quality=5):
    """Compress video - because nobody wants 4GB reaction GIFs"""
    cmd = f'ffmpeg -hide_banner -loglevel error -y -i "{input_file}" -q:v {quality} "{output_file}"'
    return run_command(cmd, f"Compressing {input_file}")

def generate_palette(input_file, palette_file="palette.png"):
    """Generate color palette - the secret sauce for quality GIFs"""
    cmd = f'ffmpeg -hide_banner -loglevel error -y -i "{input_file}" -vf "fps=15,scale=480:-1:flags=lanczos,palettegen" "{palette_file}"'
    return run_command(cmd, "Generating color palette")

def create_gif(input_file, palette_file, output_file, fps=15, width=480):
    """Create the actual GIF - where the magic happens ✨"""
    cmd = f'ffmpeg -hide_banner -loglevel error -y -i "{input_file}" -i "{palette_file}" -filter_complex "fps={fps},scale={width}:-1:flags=lanczos[x];[x][1:v]paletteuse" "{output_file}"'
    return run_command(cmd, f"Creating GIF: {output_file}")

def cleanup_temp_files(*files):
    """Clean up temporary files - keep it tidy"""
    for file in files:
        if os.path.exists(file):
            os.remove(file)
            print(f"🧹 Cleaned up {file}")

def main():
    parser = argparse.ArgumentParser(
        description="Convert videos to high-quality GIFs with ffmpeg",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s input.mp4                          # Basic conversion
  %(prog)s input.mp4 -o reaction.gif          # Custom output name
  %(prog)s input.mp4 -w 720 -f 20             # Higher quality/fps
  %(prog)s input.mp4 --compress -q 3          # Compress first, better quality
  %(prog)s input.mp4 --no-cleanup             # Keep temp files
        """
    )
    
    parser.add_argument("input", help="Input video file")
    parser.add_argument("-o", "--output", help="Output GIF file (default: input_name.gif)")
    parser.add_argument("-w", "--width", type=int, default=480, help="Output width in pixels (default: 480)")
    parser.add_argument("-f", "--fps", type=int, default=15, help="Output framerate (default: 15)")
    parser.add_argument("-q", "--quality", type=int, default=5, choices=range(1, 32), 
                       help="Video quality for compression (1=best, 31=worst, default: 5)")
    parser.add_argument("--compress", action="store_true", 
                       help="Compress video first (recommended for large files)")
    parser.add_argument("--no-cleanup", action="store_true", 
                       help="Keep temporary files (palette.png, compressed video)")
    
    args = parser.parse_args()
    
    # Validate input file
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"❌ Input file '{args.input}' not found!")
        sys.exit(1)
    
    # Set output filename
    if args.output:
        output_gif = args.output
    else:
        output_gif = input_path.with_suffix('.gif')
    
    print(f"🎬 Converting '{args.input}' to '{output_gif}'")
    print(f"📐 Settings: {args.width}px width, {args.fps}fps")
    
    # Determine source file for GIF creation
    source_file = args.input
    compressed_file = None
    
    # Optional compression step
    if args.compress:
        compressed_file = f"compressed_{input_path.name}"
        if not compress_video(args.input, compressed_file, args.quality):
            sys.exit(1)
        source_file = compressed_file
    
    # Generate palette
    palette_file = "palette.png"
    if not generate_palette(source_file, palette_file):
        cleanup_temp_files(palette_file, compressed_file)
        sys.exit(1)
    
    # Create GIF
    if not create_gif(source_file, palette_file, output_gif, args.fps, args.width):
        cleanup_temp_files(palette_file, compressed_file)
        sys.exit(1)
    
    # Cleanup unless told not to
    if not args.no_cleanup:
        cleanup_temp_files(palette_file, compressed_file)
    else:
        print("🗂️  Keeping temporary files as requested")
    
    # Show file sizes for the flex
    input_size = os.path.getsize(args.input) / (1024*1024)
    output_size = os.path.getsize(output_gif) / (1024*1024)
    print(f"\n🎉 Success!")
    print(f"📊 {input_path.name}: {input_size:.1f}MB → {Path(output_gif).name}: {output_size:.1f}MB")
    
    if output_size > 10:
        print("⚠️  Large GIF detected! Consider using --compress or lower width/fps")

if __name__ == "__main__":
    main()