% rebase ('base.tpl', title = 'Igra')
% import model

<h1>
    Računska naloga
</h1>

% if odgovor:
    <h2>NAPAKA!</h2>
    <p>
        Odgovorili ste narobe! <br>
        Poskusite ponovno.
    </p>
% end


% operacija = ["+", "-", "*", "//", "%"][znak]
<form action="/racun/" method="post">
    {{"{0} {1} {2} = ".format(a, operacija, b)}} <input type="text" name="vnos">
      <button type="submit">Vnesi vrednost</button>
</form>

