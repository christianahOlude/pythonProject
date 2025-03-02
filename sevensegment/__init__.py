from sevensegments import SevenSegment


class Main:
    def run(self):
        sevensegment = SevenSegment()


        binary_input = input("Enter an 8-digit binary string: ")

        try:
            if sevensegment.validate_input(binary_input):
                if sevensegment.is_on(binary_input):
                    converted_array = sevensegment.convert_string_to_array_of_integers(binary_input)
                    display_array = sevensegment.create_display_array(converted_array)
                    sevensegment.display(display_array)
                else:
                    print("The display is off")

        except ValueError as e:
            print(e)



if __name__ == "__main__":
    main = Main()
    main.run()