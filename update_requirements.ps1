# Define the path to the requirements.txt file
$requirementsPath = ".\requirements.txt"

# Get the list of installed pip packages
$packages = & pip freeze

# Check if there are installed packages, and overwrite the file
if ($packages) {
    $packages | Out-File -FilePath $requirementsPath -Encoding utf8
    Write-Host "requirements.txt has been updated with the current pip packages."
} else {
    Write-Host "No pip packages found."
}
