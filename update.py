import os
import glob
import re

replacement = '''  <header class="fixed top-0 left-0 w-full z-50 px-4 py-4">
    <div class="max-w-7xl mx-auto glass-panel rounded-2xl px-6 py-4 flex flex-col transition-all duration-300">
      <div class="flex items-center justify-between">
        <a href="index.html" class="flex items-center gap-3 group shrink-0">
          <svg class="w-8 h-8 sm:w-10 sm:h-10 transition-transform duration-700 group-hover:rotate-180" viewBox="0 0 100 100" fill="none">
            <circle cx="50" cy="35" r="22" stroke="url(#blue-grad)" stroke-width="8" />
            <circle cx="37" cy="60" r="22" stroke="url(#bronze-grad)" stroke-width="8" />
            <circle cx="63" cy="60" r="22" stroke="#3B82F6" stroke-width="8" />
            <defs>
              <linearGradient id="blue-grad" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#00D2FF" />
                <stop offset="100%" stop-color="#3B82F6" />
              </linearGradient>
              <linearGradient id="bronze-grad" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" stop-color="#E5A885" />
                <stop offset="100%" stop-color="#C08261" />
              </linearGradient>
            </defs>
          </svg>
          <span class="font-extrabold text-base sm:text-lg tracking-wider text-white">TRIO <span class="text-cyan-400">OPERATIX</span></span>
        </a>

        <nav class="hidden md:flex items-center gap-8 text-sm font-semibold">
          <a href="index.html" class="nav-link text-cyan-400 transition-colors">Home</a>
          <a href="capabilities.html" class="nav-link text-slate-400 hover:text-cyan-400 transition-colors">Capabilities</a>
          <a href="how-we-work.html" class="nav-link text-slate-400 hover:text-cyan-400 transition-colors">How We Work</a>
          <a href="projects.html" class="nav-link text-slate-400 hover:text-cyan-400 transition-colors">Projects</a>
          <a href="contact.html" class="nav-link text-slate-400 hover:text-cyan-400 transition-colors">Contact Us</a>
        </nav>

        <div class="flex items-center gap-2 sm:gap-4 shrink-0">
          <a href="https://wa.me/923260420276" target="_blank" class="gradient-btn px-3 py-2 sm:px-5 sm:py-2.5 rounded-xl text-xs font-bold text-black flex items-center gap-1 sm:gap-2 hover:scale-105 transition-transform shadow-lg shadow-cyan-500/20">
            <i class="fa-brands fa-whatsapp text-sm sm:text-base"></i> <span class="hidden sm:inline">WhatsApp Us</span><span class="inline sm:hidden">WhatsApp</span>
          </a>
          <button id="mobile-menu-btn" class="md:hidden text-slate-300 hover:text-white text-xl focus:outline-none p-1 ml-1" aria-label="Toggle menu">
            <i class="fa-solid fa-bars" id="menu-icon"></i>
          </button>
        </div>
      </div>
      
      <!-- Mobile Menu -->
      <nav id="mobile-menu" class="hidden md:hidden flex-col gap-4 mt-4 pb-2 text-sm font-semibold border-t border-slate-700/50 pt-4 overflow-hidden">
        <a href="index.html" class="nav-link text-cyan-400 transition-colors block">Home</a>
        <a href="capabilities.html" class="nav-link text-slate-400 hover:text-cyan-400 transition-colors block">Capabilities</a>
        <a href="how-we-work.html" class="nav-link text-slate-400 hover:text-cyan-400 transition-colors block">How We Work</a>
        <a href="projects.html" class="nav-link text-slate-400 hover:text-cyan-400 transition-colors block">Projects</a>
        <a href="contact.html" class="nav-link text-slate-400 hover:text-cyan-400 transition-colors block">Contact Us</a>
      </nav>
    </div>
  </header>'''

for f in glob.glob("*.html"):
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # replace everything between <header> and </header>
    new_content = re.sub(r'  <header class="fixed top-0 left-0 w-full z-50 px-4 py-4">.*?</header>', replacement, content, flags=re.DOTALL)
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(new_content)
        print(f"Updated {f}")
