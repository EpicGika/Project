<?php
$firstName = '';
$lastName  = '';
$email     = '';

$errors = [
    'firstNameError' => '',
    'lastNameError' => '',
    'emailError' => '',
];

if(isset($_POST["submit"])) {

        // ناخد القيم من الفورم الأول
    $firstName = $_POST["firstName"] ?? '';
    $lastName  = $_POST["lastName"] ?? '';
    $email     = $_POST["email"] ?? '';

    // تحقق الاسم الاول
    if(empty($firstName)){
        $errors["firstNameError"] = "First Name Empty";
    }
    // تحقق الاسم الاخير 
    if(empty($lastName)){
        $errors["lastNameError"] = "Last Name Empty";
    }

    // تحقق الايميل 
    if(empty($email)){
        $errors["emailError"] = "Email Empty";
    }elseif(!filter_var($email, FILTER_VALIDATE_EMAIL)){
        $errors["emailError"] = "Plase Insert Email";
    }

    // تحقق الاخطاء 
    if(!array_filter($errors)){
        $firstName =  mysqli_real_escape_string($conn, $_POST["firstName"]);
        $lastName =   mysqli_real_escape_string($conn, $_POST["lastName"]);
        $email =      mysqli_real_escape_string($conn, $_POST["email"]);

        $sql = "INSERT INTO users(firstName, lastName, email)
                VALUES ('$firstName','$lastName','$email')";

        if (mysqli_query($conn, $sql)){
        header("Location: index.php");
        }else {
        echo "Error: " . mysqli_error($conn) ;
        }
    }
}


?>


