<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link href='https://fonts.googleapis.com/css?family=Sofia' rel='stylesheet'>
<style>
body {
  margin: 0;
  font-family: Arial, Helvetica, sans-serif;
  font-weight: bolder;
  background-color: #e5c2c2d2;
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
  <a href="http://192.168.0.174:5000/">Home</a>
  <a class="active" href="http://192.168.0.174:5000/news">News</a>
  <a href="http://192.168.0.174:5000/contact">Contact</a>
  <a href="http://192.168.0.174:5000/about">About</a>
</div>

<div style="padding-left:16px">
  <h1 style="font-family: 'Sofia';" >NEWS</h1>
  <p>News and announcements on the Yoga classes will appear here.
  </p>
  <p>No news uploaded as of 20/7/20.</p>
</div>

</body>
</html>
