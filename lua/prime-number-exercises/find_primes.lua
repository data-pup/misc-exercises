function find_primes(my_int)

  local my_int = tonumber(my_int)

  -- Internal Helper Functions:
  ----------------------------------------------------------------------------

  -- This function will print the message "Prime #[n]: [prime]"
  -- given the inputs my_n, and my_prime.
  function print_n_prime(my_n, my_prime)
    print("Prime #" .. my_n .. ": " .. my_prime)
  end

  -- This function should be given an integer, and a list of primes that
  -- are less than my_int. Returns true or false.
  function find_primes_helper(my_int, my_multiples)

    -- Define an internal function for the modular operator.
    function my_mod(numerator,denominator)
      return numerator - math.floor(numerator/denominator)*denominator
    end

    -- Get the length of the multiples table that we will iterate through.
    my_length = #my_multiples

    -- Check that no numbers in the my_multiples table will divide evenly.
    for i = 1,#my_multiples
    do
      if my_int > my_multiples[i] and
        my_mod(my_int, my_multiples[i]) == 0 then
        return false
      end
    end

    -- If the loop completes, then return true.
    return true
  end

  -- Declare the looping variables for the program.
  current_value = 3
  prime_count = 0
  multiples_list = {2}

  -- This loop will create the list of prime multiples.
  repeat
    if find_primes_helper(current_value, multiples_list) == true
    then
      table.insert(multiples_list, current_value)
      prime_count = prime_count + 1
      print_n_prime(prime_count,current_value)
    end

    current_value = current_value + 1
  until current_value >= my_int

  my_return_value = find_primes_helper(my_int, multiples_list)

  if my_return_value == true
  then
    print(my_int .. " is prime.")
  else
    print(my_int .. " is not prime.")
  end

  return my_return_value
end

-- Define and invoke the main function.
function main()
  print(find_primes(arg[1]))
end

main()
