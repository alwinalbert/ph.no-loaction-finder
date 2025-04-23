#  Phone Number Tracker with Map Visualization

This project allows you to input a phone number (with country code), and it will:

- Identify the **location** (region/city) of the number.
- Identify the **carrier** (original SIM provider).
- Get the **latitude and longitude** of the location using the **OpenCage Geocoder API**.
- Plot the result on an interactive **map using Folium**, and save it as an HTML file.

>  Note: This does **not track real-time location or current carrier**. It only identifies information based on public phone number databases.

---

# 🛠️ Requirements

Install the required Python libraries using:

```bash
pip install phonenumbers opencage folium
