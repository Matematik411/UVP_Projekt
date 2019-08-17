% import model
% rebase ('base.tpl', title = 'Igra')


  <h1>Profil: <strong>{{igralec.ime.capitalize()}}</strong></h1> 

  <p>Stopnja: <strong>{{igralec.level}}</strong> <br>
  % skupno = igralec.level * 4
    Izkušnje: {{igralec.exp}} / {{skupno}}
  </p>

  <img src="/img/{{igralec.zival + str(igralec.level)}}.png/" alt="slikica" height="250">

  <p>Na voljo imate naslednje tipe nalog.</p>


  <div class="container">
    <div class="row">
      <form action="/racun/" method="post">
        <button type="submit" class="btn btn-outline-primary">Račun</button>
      </form>

      % if igralec.preostale_pesmi == []:
        <button type="button" class="btn btn-outline-primary" disabled>Pesem</button>
      % else:
        <form action="/pesem/" method="post">
          <button type="submit" class="btn btn-outline-primary">Pesem</button>
        </form>
      % end

      % if igralec.preostale_naloge == []:
        <button type="button" class="btn btn-outline-primary" disabled>Besedilna naloga</button>
      % else:
        <form action="/besedilna/" method="post">
          <button type="submit" class="btn btn-outline-primary">Besedilna naloga</button>
        </form>
      % end
    </div>
  </div>

  <p>Shrani profil in vrni na začetno stran.</p>
  <form action="/shrani/" method="post">        
    <button type="submit" class="btn btn-primary">Shrani profil</button>
  </form>

% if error:
  <div class="alert alert-warning alert-dismissible fade show" role="alert">
      Zaradi nepotrebnega <em>osveževanja</em> ali uporabljanja <em>gumba nazaj</em> je <strong>prišlo do napake!</strong><br> Ponovno izberite željeno nalogo.
      <button type="button" class="close" data-dismiss="alert" aria-label="Close">
      <span aria-hidden="true">&times;</span>
      </button>
  </div>






