# 🥋 BJJ Academy Finder 

⭐ Star this repo if it helped you find a great BJJ school!

**Professional Brazilian Jiu Jitsu school finder by ZIP code with precision rating control.**

Perfect for travelers, martial artists, and anyone seeking high-quality BJJ training. Features Google Places API integration with intelligent fallback database.

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Google Places API](https://img.shields.io/badge/Google-Places%20API-4285f4.svg)](https://developers.google.com/places/web-service)

## ✨ Features

- 🎯 **Precise ZIP code targeting** - Search exactly where you need
- ⭐ **Adjustable rating filters** - Set minimum/maximum star ratings (3.0-5.0)
- 📏 **Distance calculations** - See exact distance from ZIP center
- 📞 **Complete business info** - Phone, website, hours, price levels
- 🔍 **Quality filtering** - Automatically removes non-martial arts businesses
- 🚀 **Google Places integration** - Real-time, comprehensive data
- 💾 **Export results** - Save to JSON for analysis
- 🔄 **Smart fallback** - Works even without API key



## 🚀 Quick Start



### Installation
```bash
# Clone and navigate to project
git clone https://github.com/g3nz0d/python.git
cd python/bjj-academy-finder

# Install dependencies
pip install -r requirements.txt
```



### Basic Usage
```bash
# Find 4+ star schools in San Diego
python jiu_jitsu_academy_finder.py --zip 92120 --min-rating 4.0

# Custom rating range in Austin
python jiu_jitsu_academy_finder.py --zip 78701 --min-rating 3.5 --max-rating 4.5

# Export results
python jiu_jitsu_academy_finder.py --zip 90210 --save results.json




# Find 4+ star schools in San Diego
python jiu_jitsu_academy_finder.py --zip 92120 --min-rating 4.0

# Custom rating range in Austin
python jiu_jitsu_academy_finder.py --zip 78701 --min-rating 3.5 --max-rating 4.5

# Export results
python jiu_jitsu_academy_finder.py --zip 90210 --save results.jsonradius (meters) | `5000` (3.1 miles) |
| `--limit` | Max results | `20` |
| `--save` | Export to JSON | `results.json` |

## 🗺️ Coverage

**Curated database includes:**
- **San Diego**: 92120, 92101, 92126, 92130, 92109, 92117
- **Austin**: 78701, 78728  
- **Los Angeles**: 90210
- **New York**: 10001

Works worldwide with Google Places API (free $200 monthly credit).

---

⭐ **Star this repo if it helped you find a great BJJ school!**



🎯 Precision search in ZIP 92120
   📊 Rating range: 4.0 - 5.0 stars
   📏 Radius: 3000m (1.9 miles)

🎯 Jiu Jitsu Schools in ZIP 92120 (4.0-5.0⭐):
==================================================================================

1. Fabio Santos Brazilian Jiu Jitsu
   ⭐ Rating: 4.9/5.0 (127 reviews)
   📍 Address: 7030 Engineer Rd, San Diego, CA 92111
   📏 Distance: 2.3 miles from ZIP center
   📞 Phone: (858) 277-7644g
    ✅ Adjustable rating filters  
    ✅ Google Places API integration
    ✅ Distance calculations
    ✅ Smart fallback database
"""

__version__ = "1.0.0"
__author__ = "g3nz0d"
__license__ = "MIT"

# [Rest of your existing script content here]





🔧 Command Options
Parameter	Description	Example
--zip	ZIP code to search	92120, 78701, 10001
--min-rating	Minimum stars	4.0 (4+ stars only)
--max-rating	Maximum stars	4.5 (cap at 4.5)
--radius	Search radius (meters)	5000 (3.1 miles)
--limit	Max results	20
--save	Export to JSON	results.json





```

## 📊 Sample Output
