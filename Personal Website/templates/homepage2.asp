<!DOCTYPE html>
    <html lang="en">
        <head>
            <title>Page Title</title>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link href='https://fonts.googleapis.com/css?family=Sofia' rel='stylesheet'>
            <link rel="stylesheet" href="/w3css/3/w3.css">
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.6.3/css/font-awesome.min.css">
            <style>
            body {
                font-family: Arial, Helvetica, sans-serif;
                margin: 0;
                background-color:rgb(158,187,198);
                
            }

            /* Style the header */
            .header {
            font-family:Arial, Helvetica, sans-serif;
            padding: 80px;
            text-align: center;
            background: #1abc9c;
            color: whitesmoke;
            }

            /* Increase the font size of the h1 element */
            .header h1 {
            font-family: 'Sofia';
            font-size: 40px;
            }

            #mySidenav a {
                position: absolute;
                left: -80px;
                transition: 0.3s;
                padding: 15px;
                width: 100px;
                text-decoration: none;
                font-size: 20px;
                font-family: Arial, Helvetica, sans-serif;
                color: white;
                border-radius: 0 5px 5px 0;
                }

                #mySidenav a:hover {
                left: 0;
                }

                #about {
                top: 20px;
                background-color: #222;
                }

                #blog {
                top: 80px;
                background-color: #222;
                }

                #projects {
                top: 140px;
                background-color: #222;
                }

                #contact {
                top: 200px;
                background-color: #222;
                }
                /* Column container */
                .row {  
                display: flex;
                flex-wrap: wrap;
                }

                /* Create two unequal columns that sits next to each other */
                /* Sidebar/left column */
                .side {
                flex: 30%;
                background-color: #f1f1f1;
                font-family: Arial, Helvetica, sans-serif;
                padding: 20px;
                }

                /* Main column */
                .main {   
                flex: 70%;
                background-color: white;
                padding: 20px;
                }

                /* Fake image, just for this example */
                .fakeimg {
                background-color: #aaa;
                width: 100%;
                padding: 20px;
                }
        </style>
        </head>
        <body>

    <div class="header">
    <h1>Yoga By Marisse</h1>
    <p>Align yourself.</p>

    <div id="mySidenav" class="sidenav">
        <a href="#" id="about">About</a>
        <a href="#" id="blog">Blog</a>
        <a href="#" id="projects">Projects</a>
        <a href="#" id="contact">Contact</a>
      </div>
    </div>

    <section style="padding-left: 500px;"> 
        <img class="mySlides" src="/static/homepagepic.jpg"
        style="height: 420px;" width="350px;" >
        <img class="mySlides" src="/static/homepagepic2.jpg"
        style="height: 350px;" width="350px;"  >
        <img class="mySlides" src="/static/homepagepic3.jpg"
        style="height:350px;" width="350px" >
      </section>

      

      <script>
        // Automatic Slideshow - change image every 3 seconds
        var myIndex = 0;
        carousel();
        
        function carousel() {
          var i;
          var x = document.getElementsByClassName("mySlides");
          for (i = 0; i < x.length; i++) {
             x[i].style.display = "none";
          }
          myIndex++;
          if (myIndex > x.length) {myIndex = 1}
          x[myIndex-1].style.display = "block";
          setTimeout(carousel, 3000);
        }
        </script>
        

    </body>
</html>