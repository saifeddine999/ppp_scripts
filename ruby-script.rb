require 'json'
require 'securerandom'

def generate_point
	streets = ['USA', 'GB', 'FR', 'ES', 'PO', 'BR', 'RU']
	now = Time.now
	a_week_go = now - 60*60*24*7
	random_time = rand(a_week_go..now)
	points = {
		"id" => SecureRandom.urlsafe_base64(16),
		"doc_type" => "point",
		"location":{
			"lat" => rand(38.887563...39.887563),
			"lon" => rand(-77.019929...-76.019929),
			"point_date" => random_time.utc,
			"speed" => rand(0..100),
			"direction" => rand(1..2),
			"street" => streets.sample,
		}	
	}
end

out_file = File.new("out5.txt", "w")
2000.times do
	point = generate_point
	out_file.puts(point) 
end