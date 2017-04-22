# --------------------------------------------------------------------------- #
# This program is an implementation of a cash register, using Ruby 2.0.0p648
# Given a total price, as well as an amount given by the customer, this
# program will return the change due to the customer.
#
# Usage instructions:
#   This program should be called from the command line, with arguments.
# Example: ruby cash_register.rb -p 1.75 -g 4.99
# --------------------------------------------------------------------------- #


# # # Global Variables:
# --------------------------------------------------------------------------- #

# This array contains the values of different denominations
# that the cash register will return in change.
$register_denominations = [20, 10, 5, 1, 0.25, 0.10, 0.05, 0.01].freeze

# We will create a hash table, storing the count of each currency denomination
# i.e. 2 quarters and 3 pennies. Use this for counting change.
$change_due = Hash.new()

# # # Helper Functions:
# --------------------------------------------------------------------------- #

# This function will print usage information if the
# command line parameters are not correctly formed.
def print_usage_information
  puts "This program expects to be given two inputs when invoked."
  puts "Usage information:"
  puts "\t-p --price:\tThis is the cost of the items purchased."
  puts "\t-g --given:\tThis is the amount paid by the customer."
  puts "\t-h --help:\tDisplau this help information."
  puts "This program will find the way to break the change due,"
  puts "using standard USD $ denominations."
end


# This function will parse the ARGV array, and look for the input values
# given by the user. This function returns a float (accurate to two decimal points)
# representing the total change due.
def parse_argv

  # These are the flags that can be set within ARGV.
  help_flags = ["-h", "--help"]
  price_flags = ["-p", "--price"]
  given_flags = ["-g","--given"]

  # First, check if any help flags are present within the argv array.
  help_flags.each { |help_flag|
    if ARGV.index(help_flag) != nil
      puts "Usage info called using help flag..."
      print_usage_information()
      exit
    end
  }

  # Second, check that there is a valid number of elements in the ARGV array.
  if ARGV.length != 4
    puts "Usage information called due to ARGV length..."
    print_usage_information()
    exit
  end

  # Find ARGV indices of the price and given flags. (Determine input order.)
  price_flag_index = nil
  price_flags.each { |price_flag|
    if ARGV.index(price_flag) != nil
      price_flag_index = ARGV.index(price_flag)
    end
  }

  given_flag_index = nil
  given_flags.each { |given_flag|
    if ARGV.index(given_flag) != nil
      given_flag_index = ARGV.index(given_flag)
    end
  }

  # If either value is nil, then the input given is not correctly formed.
  if (price_flag_index == nil) || (given_flag_index == nil)
    puts "Usage information called due to missing arguments..."
    print_usage_information()
    exit
  end

  # Use the flag indices to identify the input values for the program.
  price_value_index = price_flag_index + 1
  given_value_index = given_flag_index + 1

  # Check that the value indices are within the correct range, or exit.
  if (price_value_index >= ARGV.length) || (price_value_index <= 0) ||
      (given_value_index >= ARGV.length) || (given_value_index <= 0)
      print_usage_information()
      exit
  end

  # Finally, set the registers price/given global values, and return.
  register_price = ARGV[price_value_index].to_f.round(2)
  register_given = ARGV[given_value_index].to_f.round(2)

  return (register_given - register_price).round(2)
end


# This function is used to help find the change due.
# INPUT: A single floating point number greater than 0.
# OUTPUT: No output. This will set the values in the change Hash table,
# associated with each denomination, to return the change due.
def break_change(total_change_due)
  running_total = total_change_due
  $register_denominations.each { |my_denom|
      if running_total <= 0.0
        $change_due[my_denom] = 0
      end
      current_denom_count = (running_total/my_denom).to_f.floor
      $change_due[my_denom] = current_denom_count
      running_total = running_total % my_denom
  }
end


# This function will print the results of the calculation.
def print_output
  puts "Change due:"
  total = 0.00
  $register_denominations.each { |my_denom|
    puts "\t#{$change_due[my_denom]} x $#{my_denom.round(2)}"
    total = total + ($change_due[my_denom] * my_denom)
  }
  puts "Total: #{total.round(2)}"
end


# Define main function.
# --------------------------------------------------------------------------- #
def main
  puts "Welcome to the tiny Ruby register!"
  total_change_due = parse_argv
  break_change(total_change_due)
  print_output
end


# Invoke main function.
# --------------------------------------------------------------------------- #
main()
