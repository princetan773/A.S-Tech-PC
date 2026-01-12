from flask import Flask, render_template_string

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>A.S Tech PC | ROG Style</title>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap" rel="stylesheet">
<style>
/* GENERAL STYLES */
body {
  margin: 0;
  font-family: 'Orbitron', sans-serif;
  background-color: #0a0a0a;
  color: #fff;
}
a { text-decoration: none; }
html { scroll-behavior: smooth; }

/* HERO SECTION */
.hero {
  height: 90vh;
  background: url('https://images.unsplash.com/photo-1550745165-9bc0b252726f?auto=format&fit=crop&w=1920&q=80') center/cover no-repeat;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  position: relative;
}
.hero::after {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(0,0,0,0.85);
}
.hero-content {
  position: relative;
  z-index: 1;
}
.brand-top {
  color: #fff;
  font-size: 1.2rem;
  letter-spacing: 8px;
  text-transform: uppercase;
  margin-bottom: 10px;
  display: block;
  text-shadow: 0 0 5px #fff;
}
.hero h1, .hero p {
  color: #ff0000;
  text-shadow: 0 0 10px #ff0000;
}
.hero h1 { font-size: 4rem; margin-bottom: 20px; }
.hero p { font-size: 1.5rem; }

/* NAVBAR */
nav {
  background: #111;
  display: flex;
  justify-content: center;
  gap: 30px;
  padding: 15px;
  position: sticky;
  top: 0;
  z-index: 10;
  border-bottom: 1px solid #ff0000;
}
nav a {
  color: #ff0000;
  font-weight: bold;
  transition: 0.3s;
}
nav a:hover { color: #fff; text-shadow: 0 0 10px #ff0000; }

/* SECTIONS */
section { padding: 60px 20px; max-width: 1200px; margin: auto; }
h2 { color: #ff0000; margin-bottom: 40px; text-shadow: 0 0 5px #ff0000; }

/* GRID / CARDS */
.grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 30px; }
.card {
  background: #111;
  padding: 20px;
  border: 2px solid #ff0000;
  border-radius: 15px;
  box-shadow: 0 0 15px #ff0000;
  transition: transform 0.3s, box-shadow 0.3s;
  display: flex;
  flex-direction: column;
}
.card:hover {
  transform: translateY(-10px);
  box-shadow: 0 0 30px #ff0000;
}
.card img { 
  width: 100%; 
  height: 200px; 
  border-radius: 10px; 
  margin-bottom: 15px; 
  object-fit: cover;
  border: 1px solid #333;
}
.card h3 { color: #ff0000; margin-top: 0; }

/* CTA BUTTON */
.cta {
  background: #111;
  border-radius: 20px;
  padding: 50px;
  text-align: center;
  box-shadow: 0 0 20px #ff0000;
  margin-top: 40px;
}
.cta h2 { font-size: 2.5rem; margin-bottom: 15px; color: #ff0000; text-shadow: 0 0 10px #ff0000; }
.cta-button {
  background: #ff0000;
  border: none;
  padding: 15px 40px;
  border-radius: 30px;
  font-size: 1rem;
  font-weight: bold;
  cursor: pointer;
  color: #000;
  box-shadow: 0 0 15px #ff0000;
  transition: 0.3s;
  display: inline-block;
}
.cta-button:hover {
  box-shadow: 0 0 30px #ff0000;
  transform: scale(1.05);
}

/* FOOTER */
footer {
  background: #111;
  padding: 30px;
  text-align: center;
  font-size: 0.9rem;
  color: #ff0000;
  box-shadow: 0 0 15px #ff0000 inset;
  margin-top: 60px;
}
</style>
</head>
<body>

<div class="hero">
  <div class="hero-content">
    <span class="brand-top">A.S Tech PC</span>
    <h1>Build Your Dream PC</h1>
    <p>Gaming • Creator • Office • Custom Builds</p>
  </div>
</div>

<nav>
  <a href="#services">Services</a>
  <a href="#products">Hardware</a>
  <a href="#accessories-new">Accessories</a>
  <a href="#about">About</a>
  <a href="#contact">Contact</a>
</nav>

<section id="services">
  <h2>Our Services</h2>
  <div class="grid">
    <div class="card">
      <img src="https://images.unsplash.com/photo-1593640408182-31c70c8268f5?auto=format&fit=crop&w=600&q=80" alt="Custom PC">
      <h3>Custom PC Builds</h3>
      <p>High-performance gaming and workstation systems tailored to you.</p>
    </div>
    <div class="card">
      <img src="https://images.unsplash.com/photo-1603302576837-37561b2e2302?auto=format&fit=crop&w=600&q=80" alt="Alienware Laptop">
      <h3>Repair & Upgrades</h3>
      <p>Professional diagnostics, GPU upgrades, and system cleaning.</p>
    </div>
    <div class="card">
      <img src="https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=600&q=80" alt="Business Solutions">
      <h3>Business Solutions</h3>
      <p>Reliable office setups and professional workstation hardware.</p>
    </div>
  </div>
</section>

<section id="products">
  <h2>Hardware Arsenal</h2>
  <div class="grid">
    <div class="card">
      <img src="https://images.unsplash.com/photo-1587202372775-e229f172b9d7?auto=format&fit=crop&w=600&q=80" alt="Gaming PCs">
      <h3>Gaming PCs</h3>
      <p>Pre-built monsters ready for 4K gaming and streaming.</p>
    </div>
    <div class="card">
      <img src="https://images.unsplash.com/photo-1591489378430-ef2f4c626b35?auto=format&fit=crop&w=600&q=80" alt="High-End Components">
      <h3>High-End Components</h3>
      <p>Latest RTX GPUs, DDR5 RAM, and high-speed NVMe SSDs.</p>
    </div>
    <div class="card">
      <img src="https://images.unsplash.com/photo-1598550463415-d397fdddc3e0?auto=format&fit=crop&w=600&q=80" alt="Gaming Monitor">
      <h3>Displays</h3>
      <p>High refresh rate, low latency gaming monitors.</p>
    </div>
  </div>
</section>

<section id="accessories-new">
  <h2>Accessories</h2>
  <div class="grid">
    <div class="card">
      <img src="https://images.unsplash.com/photo-1542751371-adc38448a05e?auto=format&fit=crop&w=600&q=80" alt="Tactical RGB Gaming Keyboard">
      <h3>Tactical Keyboards</h3>
      <p>Mechanical switches with intense RGB for ultimate precision.</p>
    </div>
    <div class="card">
      <img src="https://images.unsplash.com/photo-1613141411244-0e4ac259d217?auto=format&fit=crop&w=600&q=80" alt="Precision RGB Mouse">
      <h3>Precision Mice</h3>
      <p>High DPI sensors with customizable RGB lighting profiles.</p>
    </div>
    <div class="card">
      <img src="https://images.unsplash.com/photo-1612444530582-fc66183b16f7?auto=format&fit=crop&w=600&q=80" alt="Immersive RGB Headset">
      <h3>Immersive Headsets</h3>
      <p>Spatial audio with comfortable, glowing RGB earcups.</p>
    </div>
  </div>
</section>

<section id="about">
  <h2>About A.S Tech PC</h2>
  <p>We are dedicated to providing the Malaysian gaming community with the highest quality hardware and expert craftsmanship. Every build is tested for stability and performance.</p>
</section>

<section id="contact">
  <div class="cta">
    <h2>Ready to Level Up?</h2>
    <p>Talk to our experts today via WhatsApp for a custom quote.</p>
    <a href="https://wa.me/601139139199" target="_blank" class="cta-button">WHATSAPP US NOW</a>
  </div>
</section>

<footer>© 2026 A.S Tech PC. Expertly Forged in Malaysia.</footer>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == "__main__":
    app.run(debug=True)
