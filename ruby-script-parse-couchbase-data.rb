require 'json'
require 'securerandom'

def parse_data
	line_num=0
	text=File.open('out.txt').read
	text.gsub!(/\r\n?/, "\n")
	out_file = File.new("out-parse.txt", "w")
	text.each_line do |line|
		data_hash = JSON.parse(line.gsub(':location', '"location"').gsub('"point_date"=>', '"point_date"=>"').gsub(', "speed"', '", "speed"').gsub('=>', ':'))
		out_file.puts("#{data_hash['id']}\t#{data_hash['location']['lat']}\t#{data_hash['location']['lon']}\t#{data_hash['location']['point_date']}\t#{data_hash['location']['street']}\t#{data_hash['location']['speed']}")
	end
end


parse_data