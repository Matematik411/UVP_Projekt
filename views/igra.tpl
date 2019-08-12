% import model
% rebase ('base.tpl', title = 'Igra')

  <h1>Igra</h1>



  <h2>{{igralec.ime}}</h2> 


  Stopnja: {{igralec.level}} <br>
  % skupno = igralec.level * 5
  Izkušnje: {{igralec.exp}} / {{skupno}}
  
  %#<img src="/img/poro.png/" alt="slikica">

  <p>Na voljo imate naslednje tipe nalog.</p>

  <form action="/racun/" method="post">
    <button type="submit">Račun</button>
  </form>
  <form action="/pesem/" method="post">
    <button type="submit">Pesem</button>
  </form>



  <p>Shrani profil in vrni na začetno stran.</p>
  <form action="/shrani/" method="post">        
    <button type="submit">Shrani profil</button>
  </form>








