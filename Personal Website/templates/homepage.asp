<html>

    <head>

        <title>HOMEPAGE</title>
        
       

        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href='https://fonts.googleapis.com/css?family=Sofia' rel='stylesheet'>

        <style>
            
            * {box-sizing: border-box;}

            body{

                background-color: #FDDFDF;
                font-family: 'Sofia';
                font-weight:bolder;

            }

            .sidenav {
                height: 100%;   
                width: 0;
                position: fixed;
                z-index: 1;
                top: 0;
                left: 0;
                background-color: #111;
                overflow-x: hidden;
                transition: 0.5s;
                padding-top: 60px;
            }

            .sidenav a {
                padding: 8px 8px 8px 32px;
                text-decoration: none;
                font-family:Arial, Helvetica, sans-serif;
                font-size: 25px;
                color: #818181;
                display: block;
                transition: 0.3s;
            }

            .sidenav a:hover {
                color: #f1f1f1;
            }

            .sidenav .closebtn {
                position: absolute;
                top: 0;
                right: 25px;
                font-size: 36px;
                margin-left: 50px;
            }

            #main {
                transition: margin-left .5s;
                padding: 16px;
            }

            @media screen and (max-height: 450px) {
                .sidenav {padding-top: 15px;}
                .sidenav a {font-size: 18px;}
            }
        </style>
        </head>
        <body>
            <div id="mySidenav" class="sidenav">
                <a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a>
                <a href="#">About</a>
                <a href="#">Services</a>
                <a href="#">Clients</a>
                <a href="#">Contact</a>
              </div>
              
              <div id="main">
              
                <span style="font-size:30px;cursor:pointer" style="font-family: Arial, Helvetica, sans-serifs;" style="font-weight: bold;" onclick="openNav()">&#9776; Yoga By Marisse</span>
              </div>
              
              <script>
              function openNav() {
                document.getElementById("mySidenav").style.width = "250px";
                document.getElementById("main").style.marginLeft = "250px";
              }
              
              function closeNav() {
                document.getElementById("mySidenav").style.width = "0";
                document.getElementById("main").style.marginLeft= "0";
              }
              </script>
                 
        </body>
</html>