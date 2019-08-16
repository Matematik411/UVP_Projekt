% rebase ('base.tpl', title = 'Igra')

  <h1>Igra</h1>

  <blockquote>
    Pozdravljeni v igri evolucije, kjer skozi reševanje nalog razvijate svojega prijatelja. 
    <small>Velenje, avgust 2019</small>
  </blockquote>

  Za novega igralca vnesite ime in izberite prijatelja.
  <form action="/nov_igralec/" method="post">
    Ime: <input type="text" name="ime">
    
    <div class="input-group d-inline-flex" style="width: 150px" >
        <select class="custom-select" name="zival">
            <option selected >izberi prijatelja</option>
                <option value="zaba">žaba</option>
                <option value="zmaj">zmaj</option>
                <option value="kamenko">kamenko</option>
                <option value="duh">duh</option>
        </select>
    </div>

    <button type="submit" class="btn btn-primary">Nov igralec</button>
  </form>

  % if nadzor.igralci != {}:
      Če želite nadaljevati igro od prej, izberite svoje ime.
  
      %  for igralec in nadzor.igralci.values():
      <form action="/izbira/" method="post">        
        <button type="submit" name="ime" value={{igralec.ime}} class="btn btn-outline-primary">{{igralec.ime}}</button>
      </form> 
      % end

  % end




  <p>Za dodajanje nalog kliknite na spodnji gumb.</p>
  <form action="/dodaj/" method="get">        
    <button type="submit" class="btn btn-primary">Dodajanje nalog</button>
  </form>


