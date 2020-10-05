<!DOCTYPE html>
<html lang="en">
<head>
<title>Page Title</title>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link href='https://fonts.googleapis.com/css?family=Sofia' rel='stylesheet'>
<style>
* {
  box-sizing: border-box;
}

/* Style the body */
body {
  font-family:Arial, Helvetica, sans-serif;
  margin: 0;
}

/* Header/logo Title */
.header {
  padding: 80px;
  text-align: center;
  border-bottom: solid;
  background-color: #e5c2c2d2;
  color: #222;
}

/* Increase the font size of the heading */
.header h1 {
  font-size: 50px;
  font-family: 'Sofia';
}

.topnav {
  overflow: hidden;
  background-color: #333;
}

.topnav a {
  float: left;
  color: #f2f2f2;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
  font-size: 17px;
}

.topnav a:hover {
  background-color: #ddd;
  color: black;
}

.topnav a.active {
  background-color: #e5c2c2;
  color: #222;
}

/* Column container */
.row {  
  display: -ms-flexbox; /* IE10 */
  display: flex;
  -ms-flex-wrap: wrap; /* IE10 */
  flex-wrap: wrap;
}

/* Create two unequal columns that sits next to each other */
/* Sidebar/left column */
.side {
  -ms-flex: 30%; /* IE10 */
  flex: 30%;
  font-family: Arial, Helvetica, sans-serif;
  border:thin;
  border-right: hidden;
  background-color:  hsl(0, 30%, 75%);
  padding: 20px;
}

/* Main column */
.main {   
  -ms-flex: 70%; /* IE10 */
  flex: 70%;
  border:hsl(0, 30%, 75%) ;
  border:thin;
  background-color:  #e5c2c2;
  padding: 20px;
}

/* Fake image, just for this example */
.fakeimg {
  background-color:lightslategrey;
  width: 100%;
  padding: 20px;
}

/* Footer */
.footer {
  padding: 20px;
  text-align: center;
  color: whitesmoke;
  background: #111;
}

/* Responsive layout - when the screen is less than 700px wide, make the two columns stack on top of each other instead of next to each other */
@media screen and (max-width: 700px) {
  .row {   
    flex-direction: column;
  }
}

/* Responsive layout - when the screen is less than 400px wide, make the navigation links stack on top of each other instead of next to each other */
@media screen and (max-width: 400px) {
  .navbar a {
    float: none;
    width: 100%;
  }
}
</style>
</head>
<body>
  <div class="topnav">
    <a class="active" href="http://192.168.0.174:5000/">Home</a>
    <a  href="http://192.168.0.174:5000/news">News</a>
    <a href="http://192.168.0.174:5000/contact">Contact</a>
    <a href="http://192.168.0.174:5000/about">About</a>
  </div>
<div class="header">
 
   
  <h1>Yoga By Marisse</h1>
  <p style="font-weight: bold;">Yoga made simple.</p>

</div>


  

<div class="row">
  <div class="side">
    <h2>About the Instructor!</h2>
    <h5>Marisse Coutinho Bhobe</h5>
    <img src="/static/homepagepic2.jpg" style="width: 100%;" style="padding: 20px;">
    <p>Marisse Coutinho Bhobe is a goan Yoga Instructor based Dona Paula, Goa who speializes in the Iyengar style of Yoga. She started her classes in 2011, and has been teaching ever since.</p>
    <h3>Facts and Figures</h3>
    <p>Social:</p>
    <div class="fakeimg" style="height:60px;">Instagram: @marisse7</div><br>
    <div class="fakeimg" style="height:60px;">Facebook: Marisse Coutinho Bhobe</div><br>
    <div class="fakeimg" style="height:60px;">Email: marisse@bhobe.in</div>
  </div>
  <div class="main">
    <h2>BEGINNER FRIENDLY CLASS</h2>
    <h5>Strengthen your base!</h5>
    <img src="/static/homepagepic3.jpg" style="width: 100%;" style="padding: 20px;">
    <p>A note on the slower paced class:</p>
    <p>
      Along with intensive Yoga classes, Marisse conducts a class dedicated to beginners starting out with Yoga. This class is designed in a more relaxed manner such that beginners of all ages can keep up with the instructor. This is also an advantage for the slightly older students.</p>
    <br>
    <h2>TITLE HEADING</h2>
    <h5>Title description, blah blah</h5>
    <div class="fakeimg" style="height:200px;">Image</div>
    <p>Some text..</p>
    <p>
        Utilisez translate.com pour traduire des mots, des phrases et des textes entre plus de 90 paires de langues. Vous pouvez utiliser notre dictionnaire avec des exemples et obtenir la prononciation ...</p>
  </div>
</div>

<div class="footer">
  <h2>developed by Aryan Isaac Bhobe</h2>
  <h5>Instagram: @isaac.aryan007</h5>
  <h5>Twitter: @isaac_aryan</h5>
</div>

</body>
</html>
