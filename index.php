<?php
include("./inc/db.php");

if (isset($_POST["submit"])) {
    $firstName = $_POST["firstName"];
    $lastName = $_POST["lastName"];
    $email = $_POST["email"];
    //echo $firstName . " " . $lastName . " " . $email;

    $sql = "INSERT INTO users(firstName, lastName, email)
            VALUES ('$firstName','$lastName','$email')";

    mysqli_query($conn, $sql);
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="./css/style.css">
    <title>Document</title>
</head>
<body>
    <form action="index.php" method="POST">
        <input type="text" name="firstName" id="firstName" placeholder="First Name">
        <br>
        <input type="text" name="lastName" id="lastName" placeholder="Last Name">
        <br>
        <input type="email" name="email" id="email" placeholder="Email">
        <br>
        <input type="submit" name="submit" value="Send">
    </form>

    <script src="./js/script.js"></script>
</body>
</html>