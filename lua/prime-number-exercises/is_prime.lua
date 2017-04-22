-- This function will loop and print a prime number when
-- a prime number is found. Keep a count of how many primes have been found.
-- Once the loop_limit is reached, break the loop and return.
function is_prime(my_int)
  -- TODO: Declare loop variables. prime_counter = 0, current_value = 3
  -- TODO: Are these starting points sensible?

  -- Internal Helper Functions:
  ----------------------------------------------------------------------------
  -- Define an internal function for the modular operator.
  function my_mod(numerator,denominator)
    return numerator - math.floor(numerator/denominator)*denominator
  end

  -- Check that no numbers less than my_int will divide evenly.
  for i = 2,my_int-1
  do
    if my_mod(my_int, i) == 0 then
      print(my_int .. " is not prime.")
      return false
    end
  end

  -- If the loop completes, then return true.
  print(my_int .. " is prime.")
  return true
end

-- Define and invoke the main function.
function main()
  print(is_prime(arg[1]))
end

main()
