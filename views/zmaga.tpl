% import model
% rebase ('base.tpl', title = 'Igra')


  <div class="alert alert-success" role="alert">
    <h4 class="alert-heading">Čestitke {{igralec.ime.capitalize()}}!</h4>
    <p>Uspelo se vam je prebiti do konca igre! Vaš prijatelj se je razvil v močno odraslo žival, vi pa ste mu na tej poti vselej stali ob strani.</p>
    <hr>
    <p class="mb-0">Za nagrado vam podarjam okusno torto!</p>
  </div>

  <img src="/img/cake.png/" alt="torta" height="400">


  <div class="alert alert-light" role="alert">
    Igra je bila narejena kot projektna naloga pri predmetu Uvod v programiranje, pri prof. dr. Andreju Bauerju, v študijskem letu 2018/2019.
    Za pomoč se zahvaljujem družini, podatke in informacije pa sem pridobil na predavanjih in vajah že omenjenega predmeta in na svetovnem spletu.
    <br>Avtor: Nejc Zajc.
    <hr>
    Upam, da ste se ob reševanju nalog zabavali. <br>
    <em><strong>That's all Folks!</strong></em>
  </div>


  <form action="/shrani/" method="post">        
    <button type="submit" class="btn btn-dark">Nazaj na začetno stran.</button>
  </form>




