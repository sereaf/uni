function list_courses_by_teacher($teacher) {
    Write-Host "$teacher kurzusai:"
    Get-Content teams.dat -Encoding UTF8 | Select-String $teacher | ForEach-Object { $_.ToString().Split(",")[0] }
}

function list_teachers_for_student($student) {
    Write-Host "$student tanárjai:"
    Get-Content hallgato.dat -Encoding UTF8 | Select-String $student | ForEach-Object {
        $neptun_code, $course_codes = $_.ToString().Split(",")
        $codes_array = $course_codes.Split(",")
        foreach ($code in $codes_array) {
            $teacher = Get-Content teams.dat -Encoding UTF8 | Select-String $code | ForEach-Object { $_.ToString().Split(",")[2] }
            if ($teacher) {
                Write-Host $teacher
            }
        }
    }
}

function most_courses() {
    $teachers = Get-Content teams.dat -Encoding UTF8 | ForEach-Object { $_.ToString().Split(",")[2] } | Sort-Object | Get-Unique
    $max_count = 0
    $max_teacher = ""
    foreach ($teacher in $teachers) {
        $count = (Get-Content teams.dat -Encoding UTF8 | Select-String $teacher).Count
        if ($count -gt $max_count) {
            $max_count = $count
            $max_teacher = $teacher
        }
    }
    Write-Host "Tanár a legtöbb kurzussal: $max_teacher, Kurzusok száma: $max_count"
}

switch ($args[0]) {
    "-lista" {
        list_courses_by_teacher $args[1]
        break
    }
    "-hallgato" {
        list_teachers_for_student $args[1]
        break
    }
    "-sok" {
        most_courses
        break
    }
    default {
        exit 1
    }
}
