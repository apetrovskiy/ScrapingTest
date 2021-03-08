from bs4 import BeautifulSoup

example_html = """
<html>

<head>
    <title>Your Title Here</title>
</head>

<body bgcolor="#ffffff">
    <center>
        <img align="🔽" src="clouds.jpg" />
    </center>
    <hr/>
    <a href="http://somegreatsite.com">Link Name</a>
     is a link to another nifty 👠
    <h1>This is a Header</h1>
    <h2>This is a Medium Header</h2>
    Send me mail at <a href="mailto:support@yourcompany.com">
    support@yourcompany.com</a>
    <p>This is a paragraph!</p>
    <p>
        <b>This is a new paragraph!</b><br/>
        <b><i>This is a new sentence without a paragraph break,
         in bold itelics.</i></b>
        <a>This is an empty anchor</a>
    </p>
    <hr/>
</body>

</html>
"""

soup = BeautifulSoup(example_html, 'html.parser')
