% rebase ('base.tpl', title = 'Igra')

  <h1>Igra evolucije</h1>



  <div class="alert alert-info" role="alert">
    Pozdravljeni v igri evolucije, kjer skozi reševanje nalog razvijate svojega prijatelja. 
  </div>

  Za novega igralca vnesite (enobesedno) ime in izberite prijatelja.
  <form action="/nov_igralec/" method="post">
    <div class="container">
      <div class="row">
        <div class="input-group" style="width: 300px">
          <div class="input-group-prepend">
              <span class="input-group-text">Ime</span>
          </div>
          <input type="text" name="ime" class="form-control">
        </div>
        <div class="input-group d-inline-flex" style="width: 150px" >
            <select class="custom-select" name="zival">
                <option selected >Izberi prijatelja</option>
                    <option value="zaba">žaba</option>
                    <option value="zmaj">zmaj</option>
                    <option value="kamenko">kamenko</option>
                    <option value="duh">duh</option>
            </select>
        </div>
      </div>
    </div>
    <button type="submit" class="btn btn-primary">Nov igralec</button>
  </form>

  % if error:
    <div class="alert alert-warning alert-dismissible fade show" role="alert">
        Pozabili ste izbrati svojega <em>prijatelja</em> ali pa ste vpisali ime, pod katerim že obstaja profil. Ponovno poskusite.
        <button type="button" class="close" data-dismiss="alert" aria-label="Close">
        <span aria-hidden="true">&times;</span>
        </button>
    </div>
  % end
  <hr>
  
  % if nadzor.igralci != {}:
      Če želite nadaljevati igro od prej, izberite svoje ime.
      % for igralec in nadzor.igralci.values():
          <form action="/izbira/" method="post">        
          % if igralec.level == 6:
            <button type="submit" name="ime" value={{igralec.ime}} class="btn btn-outline-success">{{igralec.ime.capitalize()}}</button>
          % else:
            <button type="submit" name="ime" value={{igralec.ime}} class="btn btn-outline-primary">{{igralec.ime.capitalize()}}</button>
          % end
          </form> 
      % end
  % end




  <p>Za dodajanje nalog kliknite na spodnji gumb.</p>
  <form action="/dodaj/" method="get">        
    <button type="submit" class="btn btn-primary">Dodajanje nalog</button>
  </form>

  <small>Velenje, avgust 2019</small>
