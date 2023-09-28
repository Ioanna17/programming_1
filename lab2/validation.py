def validateInput(inputFormat, inputMessage, errorMessage):
    while True:
        try:
            inputValue = inputFormat(input(inputMessage))

        except ValueError:
            print(errorMessage)
            continue
        else:
            return inputValue