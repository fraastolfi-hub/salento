/* Salento.it: menu generale. */
(function(){
  const menu = document.getElementById("menu");
  if(!menu) return;
  const apri = document.getElementById("menuApri");
  const voci = document.getElementById("menuVoci");
  const btn = [...menu.querySelectorAll(".voce-btn")];

  const chiudiPannelli = () => btn.forEach(b => {
    b.setAttribute("aria-expanded", "false");
    document.getElementById(b.getAttribute("aria-controls")).hidden = true;
  });
  const chiudiTutto = () => {
    chiudiPannelli();
    voci.classList.remove("aperto");
    apri.setAttribute("aria-expanded", "false");
    apri.setAttribute("aria-label", "Apri il menu");
  };

  btn.forEach(b => b.addEventListener("click", () => {
    const aperto = b.getAttribute("aria-expanded") === "true";
    chiudiPannelli();
    if(!aperto){
      b.setAttribute("aria-expanded", "true");
      const p = document.getElementById(b.getAttribute("aria-controls"));
      p.hidden = false;
      /* se la tendina esce dallo schermo a destra, rientra */
      p.style.left = "";
      if(getComputedStyle(apri).display === "none"){
        const fuori = p.getBoundingClientRect().right - (document.documentElement.clientWidth - 16);
        if(fuori > 0) p.style.left = -fuori + "px";
      }
    }
  }));

  apri.addEventListener("click", () => {
    const aperto = voci.classList.toggle("aperto");
    apri.setAttribute("aria-expanded", aperto);
    apri.setAttribute("aria-label", aperto ? "Chiudi il menu" : "Apri il menu");
    if(!aperto) chiudiPannelli();
  });

  document.addEventListener("click", e => { if(!menu.contains(e.target)) chiudiTutto(); });
  document.addEventListener("keydown", e => {
    if(e.key !== "Escape") return;
    const b = btn.find(x => x.getAttribute("aria-expanded") === "true");
    if(b || voci.classList.contains("aperto")){
      chiudiTutto();
      (getComputedStyle(apri).display === "none" ? b : apri).focus();
    }
  });

  menu.querySelectorAll("a").forEach(a => {
    a.addEventListener("click", () => {
      window.dataLayer = window.dataLayer || [];
      window.dataLayer.push({event:"menu_click", voce:a.textContent.trim()});
      chiudiTutto();
    });
    if(a.href.split("#")[0].replace(/index\.html$/, "") === location.href.split(/[?#]/)[0].replace(/index\.html$/, "") && !a.hash) a.setAttribute("aria-current", "page");
  });
})();

/* Salento.it: il quiz si apre in una modale da ogni pulsante. Senza script il link porta al quiz in home. */
(function(){
  if(document.documentElement.classList.contains("in-modale")) return;
  let box = null, cornice = null, torna = null;
  const chiudi = () => { if(box && box.open) box.close(); };
  const apri = (link) => {
    torna = link;
    if(!box){
      box = document.createElement("dialog");
      box.className = "qz-modale";
      box.setAttribute("aria-label", "Trova il tuo Salento");
      box.innerHTML = '<button type="button" class="qz-x" aria-label="Chiudi il quiz">×</button><iframe title="Quattro domande per trovare il tuo Salento"></iframe>';
      document.body.appendChild(box);
      cornice = box.querySelector("iframe");
      const u = new URL(link.href, location.href);
      cornice.src = u.pathname + "?modale=1";
      box.querySelector(".qz-x").addEventListener("click", chiudi);
      box.addEventListener("click", e => { if(e.target === box) chiudi(); });
      box.addEventListener("close", () => { if(torna) torna.focus(); });
    }
    box.showModal();
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push({event:"quiz_modale_open", da:location.pathname});
  };
  document.addEventListener("click", e => {
    const a = e.target.closest('a[href$="#quiz"]');
    if(!a || e.metaKey || e.ctrlKey) return;
    e.preventDefault();
    apri(a);
  });
  window.addEventListener("message", e => {
    if(cornice && e.source === cornice.contentWindow && e.data === "quiz-chiudi") chiudi();
  });
})();
