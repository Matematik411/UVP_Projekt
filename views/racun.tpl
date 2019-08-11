% rebase ('base.tpl', title = 'igra')

<h1>
    Racunska naloga
</h1>
% operacija = ["+", "-", "*", "//", "%"][znak]
<form action="/racun/" method="post">
    {{"{0} {1} {2} = ".format(a, operacija, b)}} <input type="text" name="vnos">
      <button type="submit">Vnesi vrednost</button>
</form>


