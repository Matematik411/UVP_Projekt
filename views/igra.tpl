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
    <button type="submit">Racun</button>
  </form>
  <form action="/igra/" method="get">
    <button type="submit">Pesem</button>
  </form>









