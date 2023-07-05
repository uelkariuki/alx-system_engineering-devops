#!/usr/bin/env ruby
the_file_log = ARGV[0]
sender = the_file_log.match(/\[from:([^\]]+)\]/)&.captures&.first
receiver = the_file_log.match(/\[to:([^\]]+)\]/)&.captures&.first
flags = the_file_log.match(/\[flags:([^\]]+)\]/)&.captures&.first

puts "#{sender},#{receiver},#{flags}"
