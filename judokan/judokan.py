#!/usr/bin/env python3
"""
🥋 Judokan - Judo Technique Image Generator v1.0.0

AI-powered tool for generating realistic Judo technique demonstration images.
Perfect for instructors, students, and dojos creating educational materials.

Features:
- Generate images of classic Judo throws
- Traditional dojo settings with proper gi
- Educational technique demonstrations
- Batch image generation
- Customizable belt ranks and settings

Author: g3nz0d (Zodi Tagedini)
Location: San Diego, CA
Repository: https://github.com/g3nz0d/python
License: MIT
"""

__version__ = "1.0.0"
__author__ = "g3nz0d"
__license__ = "MIT"
__repository__ = "https://github.com/g3nz0d/python"

import sys
import argparse
import requests
import json
import os
from datetime import datetime
from typing import List, Dict

class JudoTechniqueGenerator:
    """AI image generator for Judo techniques"""
    
    def __init__(self, api_key: str = None):
        """Initialize with OpenAI API key"""
        self.api_key = api_key or os.getenv('OPENAI_API_KEY')
        if not self.api_key:
            print("⚠️ Warning: No OpenAI API key found. Set OPENAI_API_KEY environment variable.")
        
        # Judo technique prompts
        self.techniques = [
            {
                "name": "O-goshi (Major Hip Throw)",
                "prompt": "two judokas executing O-goshi (Major Hip Throw). The tori (thrower) has their opponent (uke) lifted over their hip, and they are about to throw them onto the mat. The dojo setting is traditional, with tatami mats and a simple background. The judokas wear traditional white judo gi, with one having a black belt and the other a brown belt. The motion and strength of the throw are clearly depicted.",
                "size": "1024x1024"
            },
            {
                "name": "Ippon Seoi Nage (One Arm Shoulder Throw)",
                "prompt": "two judokas executing Ippon Seoi Nage (One Arm Shoulder Throw). The tori (thrower) has their opponent (uke) lifted over their back, and they are about to throw them onto the mat. The dojo setting is traditional, with tatami mats and a simple background. The judokas wear traditional white judo gi, with one having a black belt and the other a brown belt. The motion and strength of the throw are clearly depicted.",
                "size": "1024x1024"
            },
            {
                "name": "Osoto Gari (Large Outer Reap)",
                "prompt": "two judokas executing Osoto Gari (Large Outer Reap). The tori (thrower) is sweeping their opponent's leg (uke) with a large outer reap, causing the opponent to fall backward onto the mat. The dojo setting is traditional, with tatami mats and a simple background. The judokas wear traditional white judo gi, with one having a black belt and the other a brown belt. The motion and strength of the throw are clearly depicted.",
                "size": "1024x1024"
            },
            {
                "name": "Uchi Mata (Inner Thigh Throw)",
                "prompt": "two judokas executing Uchi Mata (Inner Thigh Throw). The tori (thrower) has their leg hooked inside the opponent's (uke) thigh, lifting and throwing them over the tori's hip. The dojo setting is traditional, with tatami mats and a simple background. The judokas wear traditional white judo gi, with one having a black belt and the other a brown belt. The motion and strength of the throw are clearly depicted.",
                "size": "1024x1024"
            },
            {
                "name": "Koshi Guruma (Hip Wheel)",
                "prompt": "two judokas executing Koshi Guruma (Hip Wheel). The tori (thrower) wraps their arm around the opponent's (uke) neck and lifts them over their hip to throw them onto the mat. The dojo setting is traditional, with tatami mats and a simple background. The judokas wear traditional white judo gi, with one having a black belt and the other a brown belt. The motion and strength of the throw are clearly depicted.",
                "size": "1024x1024"
            },
            { 
                "name": "Sasae Tsurikomi Ashi (Supporting Foot Lift-Pull Throw)",
                "prompt": "two judokas executing Sasae Tsurikomi Ashi (Supporting Foot Lift-Pull Throw). The tori (thrower) is lifting and pulling the opponent's (uke) foot to unbalance and throw them onto the mat. The dojo setting is traditional, with tatami mats and a simple background. The judokas wear traditional white judo gi, with one having a black belt and the other a brown belt. The motion and strength of the throw are clearly depicted.",
                "size": "1024x1024"
            },
            {
                "name": "Hiza Guruma (Knee Wheel)",
                "prompt": "two judokas executing Hiza Guruma (Knee Wheel). The tori (thrower) uses their knee to wheel the opponent (uke) onto the mat. The dojo setting is traditional, with tatami mats and a simple background. The judokas wear traditional white judo gi, with one having a black belt and the other a brown belt. The motion and strength of the throw are clearly depicted.",
                "size": "1024x1024"
            }
        ]
    
    def generate_image(self, technique: Dict, output_dir: str = "images") -> bool:
        """Generate single technique image"""
        if not self.api_key:
            print("❌ Error: OpenAI API key required for image generation")
            return False
        
        try:
            print(f"🎨 Generating: {technique['name']}")
            
            # Create output directory
            os.makedirs(output_dir, exist_ok=True)
            
            # Call OpenAI DALL-E API
            response = requests.post(
                "https://api.openai.com/v1/images/generations",
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "dall-e-3",
                    "prompt": technique["prompt"],
                    "size": technique["size"],
                    "quality": "standard",
                    "n": 1
                }
            )
            
            if response.status_code == 200:
                result = response.json()
                image_url = result["data"][0]["url"]
                
                # Download image
                img_response = requests.get(image_url)
                if img_response.status_code == 200:
                    filename = f"{technique['name'].replace(' ', '_').replace('(', '').replace(')', '')}.png"
                    filepath = os.path.join(output_dir, filename)
                    
                    with open(filepath, 'wb') as f:
                        f.write(img_response.content)
                    
                    print(f"✅ Saved: {filepath}")
                    return True
                else:
                    print(f"❌ Failed to download image for {technique['name']}")
                    return False
            else:
                print(f"❌ API Error: {response.status_code} - {response.text}")
                return False
                
        except Exception as e:
            print(f"❌ Error generating {technique['name']}: {e}")
            return False
    
    def generate_all_techniques(self, output_dir: str = "judo_techniques") -> None:
        """Generate images for all techniques"""
        print("🥋 Judokan - Judo Technique Image Generator")
        print("=" * 50)
        
        successful = 0
        total = len(self.techniques)
        
        for technique in self.techniques:
            if self.generate_image(technique, output_dir):
                successful += 1
        
        print(f"\n📊 Generation Complete: {successful}/{total} images created")
        print(f"📁 Images saved to: {output_dir}/")
    
    def list_techniques(self) -> None:
        """List all available techniques"""
        print("🥋 Available Judo Techniques:")
        print("-" * 40)
        for i, technique in enumerate(self.techniques, 1):
            print(f"{i}. {technique['name']}")
    
    def generate_specific(self, technique_name: str, output_dir: str = "images") -> None:
        """Generate specific technique by name"""
        technique = next((t for t in self.techniques if technique_name.lower() in t['name'].lower()), None)
        
        if technique:
            self.generate_image(technique, output_dir)
        else:
            print(f"❌ Technique '{technique_name}' not found")
            print("Use --list to see available techniques")


def main():
    """Main function"""
    parser = argparse.ArgumentParser(
        description="🥋 Judokan - AI Judo Technique Image Generator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Generate all technique images
  python judokan.py --generate-all
  
  # Generate specific technique
  python judokan.py --technique "O-goshi"
  
  # List available techniques
  python judokan.py --list
  
  # Custom output directory
  python judokan.py --generate-all --output my_images/

Requires OpenAI API key: export OPENAI_API_KEY="your-key-here"
        """
    )
    
    parser.add_argument('--generate-all', action='store_true', 
                       help='Generate images for all techniques')
    parser.add_argument('--technique', type=str,
                       help='Generate specific technique by name')
    parser.add_argument('--list', action='store_true',
                       help='List all available techniques')
    parser.add_argument('--output', type=str, default='judo_techniques',
                       help='Output directory for images (default: judo_techniques)')
    parser.add_argument('--api-key', type=str,
                       help='OpenAI API key (or set OPENAI_API_KEY env var)')
    
    args = parser.parse_args()
    
    # Initialize generator
    generator = JudoTechniqueGenerator(args.api_key)
    
    if args.list:
        generator.list_techniques()
    elif args.generate_all:
        generator.generate_all_techniques(args.output)
    elif args.technique:
        generator.generate_specific(args.technique, args.output)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
