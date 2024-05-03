#!/bin/bash

list_courses_by_teacher() {
    teacher=$1
    echo "$teacher kurzusai:"
    grep "$teacher" teams.dat | cut -d ',' -f 1
}

list_teachers_for_student() {
    student=$1
    echo "$student tanárjai:"
    grep "$student" hallgato.dat | while IFS=, read -r neptun_code course_codes; do
        IFS=',' read -ra codes_array <<< "$course_codes"
        for code in "${codes_array[@]}"; do
            teacher=$(grep "$code" teams.dat | cut -d ',' -f 3)
            if [ -n "$teacher" ]; then
                echo "$teacher"
            fi
        done
    done
}

most_courses() {
    most_courses_teacher=$(cut -d ',' -f 3 teams.dat | sort | uniq -c | sort -nr | head -n 1 | awk '{print $2}')
    count=$(grep "$most_courses_teacher" teams.dat | wc -l)
    echo "Tanár a legtöbb kurzussal: $most_courses_teacher, Kurzusok száma: $count"
}

while [ "$#" -gt 0 ]; do
    case "$1" in
        -lista)
            list_courses_by_teacher "$2"
            shift 2
            ;;
        -hallgato)
            list_teachers_for_student "$2"
            shift 2
            ;;
        -sok)
            most_courses
            shift
            ;;
        *)
            exit 1
            ;;
    esac
done
