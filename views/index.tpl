% rebase ('base.tpl', title = 'Igra')

  <h1>Igra</h1>

  <blockquote>
    Tralalala.
    <small>Velenje, avgust 2019</small>
  </blockquote>

  Za novega igralca vnesite ime.
  <form action="/nov_igralec/" method="post">
    Ime: <input type="text" name="ime">        
    <button type="submit">Nov igralec</button>
  </form>

  % if nadzor.igralci != {}:
      Če želite nadaljevati igro od prej, izberite svoje ime.
  
      %  for igralec in nadzor.igralci.values():
      <form action="/izbira/" method="post">        
        <button type="submit" name="ime" value={{igralec.ime}}>{{igralec.ime}}</button>
      </form> 
      {{igralec.preostale_pesmi}}  

  % end



  <form action="/shrani/" method="post">        
    <button type="submit">Shrani profile</button>
  </form>



  <p>Za dodajanje pesmi kliknite na spodnji gumb.</p>
  <form action="/dodaj/" method="get">        
    <button type="submit">Dodajanje pesmi</button>
  </form>


