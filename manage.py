#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dbproject.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

#     // Get the posted data.
# $postdata = file_get_contents("php://input");

# if(isset($postdata) && !empty($postdata))
# {
#   // Extract the data.
#   $request = json_decode($postdata);

# ...

# $sql = "INSERT INTO `COUPON`(`id`,`description`,`amount`) VALUES (null,'{$description}','{$amount}')";

#   if(mysqli_query($con,$sql))
#   {
#     http_response_code(201);
#     $policy = [
#       'description' => $number,
#       'amount' => $amount,
#       'id'    => mysqli_insert_id($con)


# Update Pseudo-code; example of updating current info on already existing coupon info

# // Get the posted data.
# $postdata = file_get_contents("php://input");

# if(isset($postdata) && !empty($postdata))
# {
#   // Extract the data.
#   $request = json_decode($postdata);
# ….
# // Update.
#   $sql = "UPDATE `COUPON` SET `description`='$description',`amount`='$amount' WHERE `id` = '{$id}' LIMIT 1";


# Delete Pseudo-code; Example of deleting already existing coupon data but first validating via ID

# // Extract, validate the id.
# $id = ($_GET['id'] !== null && (int)$_GET['id'] > 0)? mysqli_real_escape_string($con, (int)$_GET['id']) : false;

# …

# $sql = "DELETE FROM `policies` WHERE `id` ='{$id}' LIMIT 1";

