% rebase ('base.tpl', title = 'Igra')
% import model

<h1>
    Iskanje manjkajočega dela besedila
</h1>

% if odgovor:
    <h2>Imate nekaj napak</h2>
    <p>
        Odgovorili ste z naslednjimi besedami: {{vnos}} <br>
        Vaša uspešnost: {{uspeh}}
    </p>
% end

<p>Poišči manjkajoče besede in jih v zaporedju vpiši.</p>

<h2>Izvajalec: {{avtor}}. Pesem:{{naslov}}</h2>
<p>{{niz}}</p>
<form action="/pesem/" method="post">Besede loči z vejicami.<input type="text" name="vnos">
      <button type="submit">Vnesi rešitev</button>
</form>

