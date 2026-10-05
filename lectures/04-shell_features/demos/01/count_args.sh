count_args() {
    echo "Number of args: $#"
    echo ""
    echo "The arguments were:"
    for arg in "$@"; do
        echo -e -n "  "
        echo "$arg"
    done
}
