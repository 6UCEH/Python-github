source_file = "A.txt" 
destination_file = "A1.txt"  

with open(source_file, "r") as src, open(destination_file, "w") as dest:
    dest.write(src.read()) 

print(f"Contents of '{source_file}' copied to '{destination_file}'.")
