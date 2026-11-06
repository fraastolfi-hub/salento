/* Salento.it: comportamenti condivisi delle pagine interne. */
(function(){
  window.dataLayer = window.dataLayer || [];
  const track = (event, data) => window.dataLayer.push(Object.assign({event:event}, data || {}));

  /* foto: se non carica resta il fondo con la didascalia */
  document.querySelectorAll(".ph img").forEach(img => {
    const manca = () => img.parentNode.classList.add("manca");
    if(img.complete && img.naturalWidth === 0) manca();
    img.addEventListener("error", manca);
  });

  /* link del portale non ancora pronti: niente salto in cima alla pagina */
  document.addEventListener("click", e => {
    const a = e.target.closest('a[href="#"]');
    if(a) e.preventDefault();
  });

  /* filtri degli elenchi: strutture e offerte */
  const elenco = document.getElementById("elenco");
  if(elenco){
    const carte = [...elenco.querySelectorAll("[data-tag]")];
    const vuoto = document.getElementById("vuoto");
    const conta = document.getElementById("conta");
    const attivi = {};
    const applica = () => {
      let n = 0;
      carte.forEach(c => {
        const tag = c.dataset.tag.split(" ");
        const ok = Object.values(attivi).every(v => !v || tag.includes(v));
        c.hidden = !ok;
        if(ok) n++;
      });
      if(vuoto) vuoto.hidden = n > 0;
      if(conta) conta.textContent = n === 1 ? "1 proposta" : n + " proposte";
    };
    document.querySelectorAll(".filtri").forEach(g => {
      const grp = g.dataset.gruppo;
      const btn = [...g.querySelectorAll(".filtro")];
      const scegli = b => {
        btn.forEach(x => x.setAttribute("aria-pressed", x === b));
        attivi[grp] = b.dataset.v;
        applica();
      };
      btn.forEach(b => b.addEventListener("click", () => { scegli(b); track("filtro_click", {filtro:grp, valore:b.dataset.v}); }));
      const dalLink = new URLSearchParams(location.search).get(grp);
      const pre = btn.find(b => b.dataset.v === dalLink);
      if(pre) scegli(pre);
    });
    applica();
  }

  /* elenchi grandi: alloggi e attività, caricati da un file di dati */
  const lista = document.getElementById("lista");
  if(lista){
    const esc = t => String(t || "").replace(/[&<>"']/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
    const passo = 24;
    const q = document.getElementById("cQ"), tipo = document.getElementById("cTipo"), luogo = document.getElementById("cLuogo");
    const altri = document.getElementById("altri"), conta = document.getElementById("conta");
    let tutti = [], trovati = [], visti = 0;
    const carta = x => `<article class="piccola">${x.i ? `<a class="ph" href="${esc(x.u)}" target="_blank" rel="noopener" tabindex="-1" aria-hidden="true"><img src="${esc(x.i)}" alt="" loading="lazy">${x.top ? '<span class="top">Struttura Top</span>' : ""}</a>` : ""}<div class="corpo"><span class="loc">${esc(x.t)}${x.l ? " · " + esc(x.l) : ""}</span><h2><a href="${esc(x.u)}" target="_blank" rel="noopener">${esc(x.n)}</a></h2><p>${esc(x.d)}</p></div></article>`;
    const piu = () => {
      lista.insertAdjacentHTML("beforeend", trovati.slice(visti, visti + passo).map(carta).join(""));
      lista.querySelectorAll(".ph img").forEach(i => i.addEventListener("error", () => i.parentNode.classList.add("manca"), {once:true}));
      visti = Math.min(trovati.length, visti + passo);
      altri.hidden = visti >= trovati.length;
    };
    const filtra = () => {
      const k = q.value.trim().toLowerCase();
      trovati = tutti.filter(x => (!tipo.value || x.t === tipo.value) && (!luogo.value || x.l === luogo.value) && (!k || (x.n + " " + x.l + " " + x.d).toLowerCase().includes(k)));
      lista.innerHTML = ""; visti = 0;
      conta.textContent = trovati.length === 1 ? "1 risultato" : trovati.length + " risultati";
      if(trovati.length) piu();
      else { lista.innerHTML = '<p class="vuoto">Qui non troviamo niente. Riproviamo con meno filtri?</p>'; altri.hidden = true; }
    };
    const opzioni = (sel, campo) => [...new Set(tutti.map(x => x[campo]).filter(Boolean))].sort((a, b) => a.localeCompare(b, "it")).forEach(v => sel.insertAdjacentHTML("beforeend", `<option>${esc(v)}</option>`));
    fetch(lista.dataset.src).then(r => r.json()).then(d => {
      tutti = d; opzioni(tipo, "t"); opzioni(luogo, "l");
      const dalLink = new URLSearchParams(location.search).get("q");
      if(dalLink) q.value = dalLink;
      filtra();
    });
    [q, tipo, luogo].forEach(c => c.addEventListener("input", filtra));
    altri.addEventListener("click", piu);
  }

  /* hotel e case: filtri, ordinamento e pagine sulle carte già nella pagina */
  const cat = document.getElementById("catalogo");
  if(cat){
    const passo = 12;
    const form = document.getElementById("catFiltri"), lista = document.getElementById("catLista");
    const ord = document.getElementById("catOrd"), conta = document.getElementById("catConta");
    const attivi = document.getElementById("catAttivi"), vuoto = document.getElementById("catVuoto");
    const nav = document.getElementById("catPagine"), ris = document.getElementById("catRisultati");
    const apri = document.getElementById("catApri"), mostra = document.getElementById("catMostra"), num = document.getElementById("catNum");
    const carte = [...lista.children], lab = cat.dataset.etichetta;
    const multipli = ["mese", "zona", "tipo", "tratt", "stelle", "tag", "serv"], singoli = ["q", "luogo", "prezzo", "persone"];
    let pagina = 1;

    const stato = () => {
      const s = {};
      multipli.forEach(n => s[n] = [...form.querySelectorAll(`input[name="${n}"]:checked`)].map(i => i.value));
      singoli.forEach(n => { const c = form.elements[n]; s[n] = c ? c.value.trim() : ""; });
      return s;
    };
    const passa = (d, s) => {
      const k = s.q.toLowerCase();
      if(k && !d.cerca.includes(k)) return false;
      if(s.mese.length && !s.mese.includes(d.mese)) return false;
      if(s.zona.length && !s.zona.includes(d.zona)) return false;
      if(s.tipo.length && !s.tipo.includes(d.tipo)) return false;
      if(s.tratt.length && !s.tratt.some(x => (d.tratt || "").split("|").includes(x))) return false;
      if(s.stelle.length && !s.stelle.includes(d.stelle)) return false;
      if(s.luogo && d.luogo !== s.luogo) return false;
      if(s.prezzo && (!+d.prezzo || +d.prezzo > +s.prezzo)) return false;
      if(s.persone && +d.persone < +s.persone) return false;
      const serv = d.serv ? d.serv.split("|") : [], tag = d.tag ? d.tag.split("|") : [];
      return s.serv.every(x => serv.includes(x)) && s.tag.every(x => tag.includes(x));
    };
    const senzaPrezzoInFondo = (a, b, f) => (!+a.dataset.prezzo) - (!+b.dataset.prezzo) || f();
    const confronti = {
      top: (a, b) => a.dataset.rank - b.dataset.rank,
      rec: (a, b) => b.dataset.rec - a.dataset.rec || a.dataset.nome.localeCompare(b.dataset.nome, "it"),
      "pz-su": (a, b) => senzaPrezzoInFondo(a, b, () => a.dataset.prezzo - b.dataset.prezzo),
      "pz-giu": (a, b) => senzaPrezzoInFondo(a, b, () => b.dataset.prezzo - a.dataset.prezzo),
      persone: (a, b) => b.dataset.persone - a.dataset.persone,
      quando: (a, b) => a.dataset.m - b.dataset.m,
      nome: (a, b) => a.dataset.nome.localeCompare(b.dataset.nome, "it")
    };
    const scrivi = (s) => {
      const u = new URLSearchParams();
      multipli.forEach(n => s[n].forEach(v => u.append(n, v)));
      singoli.forEach(n => { if(s[n]) u.set(n, s[n]); });
      if(ord.selectedIndex > 0) u.set("ordina", ord.value);
      if(pagina > 1) u.set("pagina", pagina);
      const q = u.toString();
      history.replaceState(null, "", location.pathname + (q ? "?" + q : ""));
    };
    const leggi = () => {
      const u = new URLSearchParams(location.search);
      multipli.forEach(n => u.getAll(n).forEach(v => {
        const i = [...form.querySelectorAll(`input[name="${n}"]`)].find(x => x.value.toLowerCase() === v.toLowerCase());
        if(i) i.checked = true;
      }));
      singoli.forEach(n => { const c = form.elements[n]; if(c && u.has(n)) c.value = u.get(n); });
      if([...ord.options].some(o => o.value === u.get("ordina"))) ord.value = u.get("ordina");
      pagina = Math.max(1, parseInt(u.get("pagina"), 10) || 1);
    };
    const chip = (t, via) => {
      const b = document.createElement("button");
      b.type = "button"; b.className = "cat-chip";
      b.setAttribute("aria-label", "Togli il filtro " + t);
      b.textContent = t + " ×";
      b.addEventListener("click", () => { via(); pagina = 1; aggiorna(); });
      attivi.appendChild(b);
    };
    const disegnaAttivi = s => {
      attivi.textContent = "";
      multipli.forEach(n => s[n].forEach(v => chip(n === "stelle" ? v + " stelle" : v, () => { [...form.querySelectorAll(`input[name="${n}"]`)].find(x => x.value === v).checked = false; })));
      singoli.forEach(n => {
        if(!s[n]) return;
        const c = form.elements[n];
        chip(c.tagName === "SELECT" ? c.selectedOptions[0].textContent.replace(/\s*\(\d+\)$/, "") : "“" + s[n] + "”", () => { c.value = ""; });
      });
      const n = attivi.children.length;
      attivi.hidden = !n;
      num.textContent = n ? ` (${n})` : "";
    };
    const disegnaPagine = tot => {
      nav.textContent = "";
      nav.hidden = tot < 2;
      if(tot < 2) return;
      const vai = (t, p, opz = {}) => {
        const b = document.createElement("button");
        b.type = "button"; b.textContent = t;
        if(opz.label) b.setAttribute("aria-label", opz.label);
        if(p === pagina && !opz.freccia) b.setAttribute("aria-current", "page");
        b.disabled = opz.spento || false;
        b.addEventListener("click", () => {
          pagina = p; aggiorna();
          ris.focus({preventScroll:true}); ris.scrollIntoView();
          track("pagina_click", {pagina:p});
        });
        nav.appendChild(b);
      };
      vai("←", pagina - 1, {freccia:true, spento:pagina === 1, label:"Pagina precedente"});
      for(let i = 1; i <= tot; i++) vai(String(i), i, {label:"Pagina " + i});
      vai("→", pagina + 1, {freccia:true, spento:pagina === tot, label:"Pagina successiva"});
    };
    const aggiorna = () => {
      const s = stato();
      const buone = carte.filter(c => passa(c.dataset, s)).sort(confronti[ord.value]);
      const tot = Math.ceil(buone.length / passo);
      pagina = Math.min(pagina, Math.max(1, tot));
      const da = (pagina - 1) * passo;
      carte.forEach(c => { c.hidden = true; });
      buone.forEach((c, i) => { lista.appendChild(c); c.hidden = i < da || i >= da + passo; });
      conta.textContent = buone.length === 1 ? (cat.dataset.uno || (lab === "hotel" ? "1 hotel" : "1 casa")) : buone.length + " " + lab;
      mostra.textContent = buone.length ? (buone.length === 1 ? "Mostra il risultato" : `Mostra ${buone.length} risultati`) : "Nessun risultato";
      vuoto.hidden = buone.length > 0;
      disegnaAttivi(s); disegnaPagine(tot); scrivi(s);
    };
    const chiudi = () => { form.classList.remove("aperto"); apri.setAttribute("aria-expanded", "false"); };

    form.addEventListener("input", e => {
      pagina = 1; aggiorna();
      if(e.target.type !== "search") track("filtro_click", {filtro:e.target.name, valore:e.target.value});
    });
    form.addEventListener("submit", e => e.preventDefault());
    form.addEventListener("reset", () => setTimeout(() => { pagina = 1; aggiorna(); }));
    ord.addEventListener("input", () => { pagina = 1; aggiorna(); track("ordina_click", {valore:ord.value}); });
    apri.addEventListener("click", () => { apri.setAttribute("aria-expanded", form.classList.toggle("aperto")); });
    mostra.addEventListener("click", () => { chiudi(); ris.focus({preventScroll:true}); ris.scrollIntoView(); });
    leggi(); aggiorna();
  }

  /* mappa delle destinazioni: zone e punti accesi insieme */
  const zone = document.getElementById("zone");
  if(zone){
    const pin = [...document.querySelectorAll(".pin")], sez = [...document.querySelectorAll(".zona")];
    const btn = [...zone.querySelectorAll(".filtro")];
    btn.forEach(b => b.addEventListener("click", () => {
      const z = b.dataset.z;
      btn.forEach(x => x.setAttribute("aria-pressed", x === b));
      sez.forEach(s => { s.hidden = !!z && s.dataset.z !== z; });
      pin.forEach(p => p.classList.toggle("spento", !!z && p.dataset.z !== z));
      track("zona_click", {zona:z});
    }));
    const accendi = (s, on) => {
      document.querySelectorAll(`.pin[data-s="${s}"],.z-lista a[data-s="${s}"]`).forEach(x => x.classList.toggle("acceso", on));
    };
    document.querySelectorAll(".pin,.z-lista a").forEach(a => {
      ["mouseenter", "focus"].forEach(ev => a.addEventListener(ev, () => accendi(a.dataset.s, true)));
      ["mouseleave", "blur"].forEach(ev => a.addEventListener(ev, () => accendi(a.dataset.s, false)));
    });
  }

  /* carosello */
  const car = document.getElementById("track");
  if(car){
    const slide = car.querySelectorAll(".slide");
    const box = document.getElementById("dots");
    let cur = 0, t;
    slide.forEach((s, i) => {
      const d = document.createElement("button");
      d.className = "dot"; d.type = "button";
      d.setAttribute("aria-label", "Vai alla foto " + (i + 1));
      d.addEventListener("click", () => vai(i));
      box.appendChild(d);
    });
    const dots = box.querySelectorAll(".dot");
    const pinta = () => dots.forEach((d, i) => d.setAttribute("aria-current", i === cur ? "true" : "false"));
    const calmo = matchMedia("(prefers-reduced-motion: reduce)").matches;
    function vai(i){
      cur = (i + slide.length) % slide.length;
      car.scrollTo({left: slide[cur].offsetLeft - car.offsetLeft, behavior: calmo ? "auto" : "smooth"});
      pinta();
    }
    document.getElementById("prev").addEventListener("click", () => vai(cur - 1));
    document.getElementById("next").addEventListener("click", () => vai(cur + 1));
    car.addEventListener("keydown", e => {
      if(e.key === "ArrowRight"){ e.preventDefault(); vai(cur + 1); }
      if(e.key === "ArrowLeft"){ e.preventDefault(); vai(cur - 1); }
    });
    car.addEventListener("scroll", () => { clearTimeout(t); t = setTimeout(() => { cur = Math.round(car.scrollLeft / car.clientWidth); pinta(); }, 80); });
    pinta();
  }

  /* blocca la camera: modulo in due passi */
  const form = document.getElementById("quote");
  if(form){
    const $ = id => document.getElementById(id);
    const struttura = form.dataset.struttura;
    const richiesta = form.dataset.modo === "richiesta";
    const inD = $("arrivo"), outD = $("partenza"), s1 = $("step1"), s2 = $("step2");
    const oggi = new Date(Date.now() - new Date().getTimezoneOffset()*60000).toISOString().slice(0,10);
    inD.min = oggi; outD.min = oggi;
    inD.addEventListener("change", () => { outD.min = inD.value || oggi; });
    const mark = (id, bad) => $(id).classList.toggle("bad", bad);
    const val = n => { const c = form.elements[n]; return c ? c.value : ""; };
    const fmt = d => { const p = d.split("-"); return p[2] + "/" + p[1]; };
    const passo = n => {
      s1.hidden = n !== 1; s2.hidden = n !== 2;
      $("st1").classList.toggle("on", n === 1); $("st2").classList.toggle("on", n === 2);
    };
    const avanti = () => {
      const b1 = !inD.value || inD.value < oggi; mark("f-in", b1);
      const b2 = !outD.value || (inD.value && outD.value <= inD.value); mark("f-out", b2);
      if(b1 || b2){ (b1 ? inD : outD).focus(); return; }
      const bimbi = $("bambini").value;
      $("recap").textContent = "Dal " + fmt(inD.value) + " al " + fmt(outD.value) +
        ($("flex").checked ? " (±3 giorni)" : "") + ", " + $("adulti").value + " adulti" +
        (bimbi === "Nessuno" ? "" : " e " + bimbi + (bimbi === "1" ? " bambino" : " bambini")) +
        (val("trattamento") ? ", " + val("trattamento").toLowerCase() : "") + ".";
      passo(2);
      $("nome").focus();
      track("preventivo_step2", {struttura:struttura});
    };
    $("toStep2").addEventListener("click", avanti);
    $("toStep1").addEventListener("click", () => { passo(1); inD.focus(); });
    const canale = () => {
      const ch = val("canale");
      const tel = ch !== "Email";
      $("tel-opt").hidden = tel; $("mail-opt").hidden = !tel;
      $("f-slot").hidden = ch !== "Telefonata";
      if(!richiesta) $("sendBtn").textContent = ch === "Telefonata" ? "Richiedi e blocca, richiamatemi" : ch === "WhatsApp" ? "Richiedi e blocca su WhatsApp" : "Richiedi e blocca la camera";
      mark("f-tel", false); mark("f-mail", false);
    };
    form.querySelectorAll('input[name="canale"]').forEach(r => r.addEventListener("change", canale));
    canale();
    form.addEventListener("submit", e => {
      e.preventDefault();
      if(!s1.hidden){ avanti(); return; }
      const ch = val("canale"), n = $("nome"), em = $("email"), tel = $("tel");
      const b3 = n.value.trim().length < 2; mark("f-name", b3);
      const ok = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(em.value.trim());
      const b4 = ch === "Email" ? !ok : (em.value.trim() !== "" && !ok); mark("f-mail", b4);
      const b5 = ch !== "Email" && tel.value.replace(/[^0-9]/g, "").length < 8; mark("f-tel", b5);
      if(b3 || b4 || b5){ const f = form.querySelector(".fld.bad input"); if(f) f.focus(); return; }
      const msg = {
        Email: "ti conferma camera e prezzo per email entro domani.",
        WhatsApp: "ti conferma camera e prezzo su WhatsApp entro domani.",
        Telefonata: "ti richiama entro domani, nella fascia che hai indicato, per confermarti camera e prezzo."
      }[ch];
      $("doneMsg").textContent = form.dataset.fatto ? form.dataset.fatto : richiesta
        ? form.dataset.nome + " ti risponde con prezzo e disponibilità. Chiedere a due non costa niente. Statte bonu."
        : form.dataset.nome + " " + msg + " Da quel momento la camera è tua per 48 ore, senza pagare nulla. Statte bonu.";
      track("preventivo_submit", {struttura:struttura, trattamento:val("trattamento"), canale:ch, anche_simili:!!($("anche") && $("anche").checked)});
      /* qui: invio al gestionale dell'hotel */
      $("campi").hidden = true; $("fatto").hidden = false;
      $("fatto").focus();
    });
  }

  /* scheda hotel: foto, camera scelta e modulo a foglio su mobile */
  const gal = document.getElementById("hGal");
  if(gal){
    const box = document.createElement("dialog");
    box.className = "h-foto";
    box.setAttribute("aria-label", "Tutte le foto di " + (gal.dataset.nome || "Hotel Beach Salento"));
    box.innerHTML = '<button type="button" class="h-card-x" aria-label="Chiudi le foto">×</button><h2></h2><div class="h-foto-griglia"></div>';
    box.querySelector("h2").textContent = gal.dataset.titolo || "Com'è, prima di arrivarci";
    gal.querySelectorAll("figure").forEach(f => {
      const c = f.cloneNode(true);
      c.querySelector("img").loading = "lazy";
      box.querySelector(".h-foto-griglia").appendChild(c);
    });
    document.body.appendChild(box);
    const tutte = document.getElementById("hGalTutte");
    const apriFoto = () => { box.showModal(); box.scrollTop = 0; track("foto_tutte"); };
    if(tutte){ tutte.hidden = false; tutte.addEventListener("click", apriFoto); }
    gal.addEventListener("click", e => { if(e.target.tagName === "IMG" && !piccolo.matches) apriFoto(); });
    box.querySelector(".h-card-x").addEventListener("click", () => box.close());
    box.addEventListener("click", e => { if(e.target === box) box.close(); });
  }
  const piccolo = matchMedia("(max-width:980px)");
  const scheda = document.getElementById("preventivo");
  if(scheda && scheda.classList.contains("h-card")){
    const x = document.getElementById("hChiudi");
    const fuori = [...document.querySelectorAll("body>header,.h-col,.h-legale,body>footer,#barra")];
    let torna = null;
    scheda.classList.add("foglio");
    x.hidden = !piccolo.matches;
    const chiudi = () => {
      if(!scheda.classList.contains("aperto")) return;
      scheda.classList.remove("aperto");
      fuori.forEach(el => { el.inert = false; });
      document.documentElement.style.overflow = "";
      if(torna) torna.focus({preventScroll:true});
    };
    const apri = da => {
      torna = da;
      track("modulo_apri", {struttura:form ? form.dataset.struttura : ""});
      if(!piccolo.matches){
        const f = scheda.querySelector("#step1:not([hidden]) input, #step2:not([hidden]) input:not([type=radio])");
        if(f) f.focus();
        return;
      }
      scheda.classList.add("aperto");
      fuori.forEach(el => { el.inert = true; });
      document.documentElement.style.overflow = "hidden";
      scheda.scrollTop = 0;
      scheda.focus({preventScroll:true});
    };
    document.addEventListener("click", e => {
      const a = e.target.closest('a[href="#preventivo"]');
      if(a){ e.preventDefault(); apri(a); }
    });
    x.addEventListener("click", chiudi);
    document.addEventListener("keydown", e => { if(e.key === "Escape") chiudi(); });
    piccolo.addEventListener("change", () => { x.hidden = !piccolo.matches; if(!piccolo.matches) chiudi(); });

    const riga = document.getElementById("hScelta");
    const nomeCam = id => { const l = id && id !== "c0" ? scheda.querySelector(`label[for="${id}"]`) : null; return l ? l.textContent : ""; };
    const segna = id => { const n = nomeCam(id); riga.hidden = !n; riga.textContent = n ? "Camera scelta: " + n : ""; };
    document.querySelectorAll(".h-cam").forEach(b => b.addEventListener("click", () => {
      document.getElementById(b.dataset.camera).checked = true;
      segna(b.dataset.camera);
      track("camera_scelta", {camera:nomeCam(b.dataset.camera)});
      apri(b);
    }));
    scheda.querySelectorAll('input[name="camera"]').forEach(r => r.addEventListener("change", () => segna(r.id)));
  }

  /* cosa fare: una lista per volta, secondo con chi vieni */
  const fare = document.getElementById("mFare");
  if(fare){
    const lista = fare.querySelector(".m-tab");
    const tab = [...lista.querySelectorAll("button")];
    const scegli = (b, fuoco) => {
      tab.forEach(x => {
        const on = x === b;
        x.setAttribute("aria-selected", on);
        x.tabIndex = on ? 0 : -1;
        document.getElementById(x.getAttribute("aria-controls")).hidden = !on;
      });
      if(fuoco) b.focus();
    };
    lista.hidden = false;
    fare.classList.add("pronto");
    scegli(tab[0]);
    tab.forEach((b, i) => {
      b.addEventListener("click", () => { scegli(b); track("cosa_fare_tab", {gruppo:b.textContent}); });
      b.addEventListener("keydown", e => {
        const d = {ArrowRight:1, ArrowLeft:-1}[e.key];
        if(d){ e.preventDefault(); scegli(tab[(i + d + tab.length) % tab.length], true); }
      });
    });
  }

  /* quello che ci hai già detto nel quiz o nella ricerca non si riscrive */
  if(form){
    /* bozza: resta finché è aperta la scheda del browser, anche cambiando pagina */
    const campi = ["arrivo", "partenza", "adulti", "bambini", "nome", "email", "tel"];
    try {
      const b = JSON.parse(sessionStorage.getItem("bozza") || "{}");
      const oggiB = new Date().toISOString().slice(0, 10);
      campi.forEach(c => {
        const el = document.getElementById(c);
        if(!el || !b[c]) return;
        if(el.type === "date" && b[c] < oggiB) return;
        el.value = b[c];
      });
    } catch(e){}
    const salva = () => {
      const b = {};
      campi.forEach(c => { const el = document.getElementById(c); if(el) b[c] = el.value; });
      try { sessionStorage.setItem("bozza", JSON.stringify(b)); } catch(e){}
    };
    form.addEventListener("input", salva);
    form.addEventListener("change", salva);
    /* mesi di apertura: avvisa, non blocca */
    const avv = document.getElementById("hAvviso"), ap = form.dataset.apre, ch = form.dataset.chiude;
    if(avv && ap && ch){
      const fuori = d => { const m = d.slice(5); return !!d && (ap <= ch ? (m < ap || m > ch) : (m < ap && m > ch)); };
      const guarda = () => {
        const a = document.getElementById("arrivo").value, p = document.getElementById("partenza").value;
        const no = (a && fuori(a)) || (p && fuori(p));
        avv.hidden = !no;
        avv.textContent = no ? form.dataset.stagione : "";
      };
      form.addEventListener("change", guarda);
      guarda();
    }
    let v = null;
    try { v = JSON.parse(sessionStorage.getItem("richiesta")); } catch(e){}
    if(v){
      const ad = document.getElementById("adulti"), bi = document.getElementById("bambini"), no = document.getElementById("note");
      if(ad && v.adulti) ad.value = v.adulti;
      if(bi && v.bambini) bi.value = v.bambini;
      if(no && v.nota) no.value = v.nota;
    }
  }

  /* form di zona: si apre a foglio, da qualunque punto della pagina */
  const sezForm = document.querySelector("section.prenota#preventivo");
  const fForm = document.getElementById("quote");
  if(sezForm && fForm){
    const casa = fForm.parentNode, dopo = fForm.nextSibling;
    const foglio = document.createElement("dialog");
    foglio.className = "m-foglio";
    foglio.setAttribute("aria-label", "Invia la richiesta");
    foglio.innerHTML = '<button type="button" class="h-card-x" aria-label="Chiudi il modulo">×</button>';
    document.body.appendChild(foglio);
    let torna = null;
    const apriF = da => {
      torna = da || null;
      foglio.appendChild(fForm);
      foglio.showModal();
      track("modulo_apri", {struttura:fForm.dataset.struttura});
    };
    foglio.querySelector(".h-card-x").addEventListener("click", () => foglio.close());
    foglio.addEventListener("click", e => { if(e.target === foglio) foglio.close(); });
    foglio.addEventListener("close", () => { casa.insertBefore(fForm, dopo); if(torna) torna.focus(); });
    document.addEventListener("click", e => {
      const a = e.target.closest('a[href="#preventivo"]');
      if(a){ e.preventDefault(); apriF(a); }
    });
    const nota = document.getElementById("note");
    if(nota && fForm.dataset.nota && !nota.value) nota.value = fForm.dataset.nota;
    if(new URLSearchParams(location.search).has("richiesta")) apriF();
  }

  /* dopo l'invio: la stessa richiesta ad altre strutture */
  document.querySelectorAll(".h-ancora").forEach(b => b.addEventListener("click", () => {
    b.disabled = true;
    b.textContent = "Richiesta inviata";
    track("richiesta_extra", {da:form.dataset.struttura, a:b.dataset.a});
    /* qui: invio al gestionale della struttura */
  }));

  /* barra mobile: sparisce quando il modulo è a vista */
  const barra = document.getElementById("barra");
  const pren = document.getElementById("preventivo");
  if(barra && pren && "IntersectionObserver" in window){
    new IntersectionObserver(es => es.forEach(x => barra.classList.toggle("via", x.isIntersecting)), {threshold:.05}).observe(pren);
  }
})();
