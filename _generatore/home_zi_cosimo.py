"""Home alternativa con Zì Cosimo, per mostrarla ad Alberto. Parte da index.html: rilanciarla se la home cambia, poi menu.py."""
import os, re
B = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/"
s = open(B + "index.html", encoding="utf-8").read()

def R(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:70])
    s = s.replace(a, b)

# testa della pagina
s, n = re.subn(r"<title>.*?</title>", "<title>Zì Cosimo ti dice dove andare · Salento.it</title>", s, count=1); assert n == 1
s, n = re.subn(r'<meta name="description" content="[^"]*">', '<meta name="description" content="Zì Cosimo ti dice dove andare nel Salento, e perché. Quattro domande, un minuto: la tua marina, il perché, i contro e dove dormire.">', s, count=1); assert n == 1
# hero: titolo fisso e firma con il ritratto
i = s.index('<p class="titolo" id="titolo">'); j = s.index("</script>", i) + len("</script>")
s = s[:i] + '<p class="titolo">Ti dico dove andare. <span class="hl">E perché.</span></p>\n<script>window.HEADLINE = {id:"zi-cosimo", chiusura:"Allora, dove andiamo?"};</script>' + s[j:]
s, n = re.subn(r'<p class="lead">Dove dormire, cosa fare.*?</p>', '''<p class="lead">Quaranta marine. Per te ce n'è una. Te la dico, con il perché e con i contro.</p>
      <p class="sign"><img class="av" src="images/zi-cosimo-160.jpg" alt="Ritratto di Zì Cosimo" width="84" height="84"><span>Zì Cosimo<small>In Salento ci campa tutto l'anno, non solo ad agosto.</small></span></p>''', s, count=1, flags=re.S); assert n == 1
R('<span class="t">Quattro domande, un minuto.</span>', '<span class="t">Dimmi come sei fatto.</span>')
# risultati del quiz
R('<h2 tabindex="-1">Ti mandiamo a ${ultimi[0].m.nome}.</h2>', '<h2 tabindex="-1">Zì Cosimo ti manda a ${ultimi[0].m.nome}.</h2>')
R('<img class="av" src="images/sole.svg" alt="" width="40" height="40"><div><b>Il consiglio di chi ci vive</b>', '<img class="av" src="images/zi-cosimo-160.jpg" alt="" width="40" height="40"><div><b>Zì Cosimo</b>')
# il blocco che lo presenta
R('<!-- ===================== FIDUCIA E FAQ ===================== -->', '''<!-- ===================== ZÌ COSIMO ===================== -->
<section class="band" id="consigli">
  <div class="wrap">
    <div class="rv shead vhead">
      <img class="zc-big" src="images/zi-cosimo-640.jpg" alt="Ritratto illustrato di Zì Cosimo: canottiera bianca, occhiali scuri, barba brizzolata e mezzo sorriso" width="640" height="640" loading="lazy">
      <div>
        <h2>I consigli di Zì Cosimo</h2>
        <p>Ruvido fuori, caldo dentro: ti dice come stanno le cose e poi ti offre da bere. Diciotto anni a Milano, poi uno schianto in tangenziale e due mesi fermo a Tricase. Ora insegna a stare a chi arriva di corsa.</p>
        <p class="zc-motto">Non ti mando dove pagano. Ti mando dove impari a stare.</p>
      </div>
    </div>
    <div class="rv voices">
      <div class="voice"><p><b>Osci</b> è agosto, e il mare è di tutti. <b>Crai</b> è settembre: stessa acqua calda, metà gente, prezzi da cristiani. Se hai un bimbo piccolo, aspetta. <b>Te lu dicu ieu.</b></p></div>
      <div class="voice"><p>Il parcheggio di Pescoluse ad agosto? <b>Addhu nu mmetti piede.</b> Arriva presto, o vieni a settembre. <b>Statte bonu.</b></p></div>
      <div class="voice"><p>Il pasticciottu si mangia caldo, la mattina, seduto. In piedi non vale. Dove? <b>Conosco a uno.</b></p></div>
    </div>
    <p class="rv zc-nota"><b>Zì Cosimo è un personaggio. I consigli no.</b> Dietro ci sono i salentini che verificano le marine, d'inverno e d'estate.</p>
  </div>
</section>

<!-- ===================== FIDUCIA E FAQ ===================== -->''')
css = '''
.sign{display:flex;align-items:center;gap:12px;margin:18px 0 0;font-size:1rem;font-weight:800;color:var(--white)}
.av{flex:none;display:block;border-radius:50%;object-fit:cover;object-position:50% 28%;background:var(--sun)}
.sign .av{width:84px;height:84px;border:3px solid var(--sun)}
.sign small{display:block;margin-top:2px;font-size:.92rem;font-weight:400;color:rgba(255,255,255,.88)}
.zc .av{width:40px;height:40px}
.vhead{display:flex;justify-content:flex-start;align-items:center;flex-wrap:nowrap;gap:clamp(20px,3vw,32px)}
.zc-big{flex:none;width:clamp(140px,16vw,210px);height:auto;aspect-ratio:1;border-radius:var(--r);object-fit:cover;display:block}
.zc-motto{margin-top:10px !important;font-size:1.25rem !important;font-weight:800;line-height:1.25;color:var(--red-d) !important}
.voices{display:grid;grid-template-columns:1.3fr 1fr 1fr;gap:16px}
.voice{background:var(--navy);color:var(--white);border-radius:var(--r);padding:24px;display:flex;flex-direction:column;gap:18px}
.voice p{font-size:1.1rem;line-height:1.5;font-weight:500}
.voice:first-child p{font-size:1.3rem;line-height:1.42}
.voice p b{font-weight:800;color:var(--sun)}
.zc-nota{margin-top:18px;font-size:.96rem;color:var(--muted)}
.zc-nota b{color:var(--navy)}
@media (max-width:760px){.voices{grid-template-columns:1fr}.vhead{flex-direction:column;align-items:flex-start}}
'''
i = s.index("</style>")
s = s[:i] + css + s[i:]
open(B + "home-zi-cosimo.html", "w", encoding="utf-8").write(s)
print("home con Zì Cosimo scritta")
