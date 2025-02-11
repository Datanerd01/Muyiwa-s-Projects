def calculate_area(side_length):
    return side_length ** 2

# Streamlit app
def main():
    st.title("Square Area Calculator")
    
    # Input: side length of the square
    side_length = st.number_input("Enter the side length of the square:", min_value=0.0, step=0.1)
    
    # Calculate area
    if st.button("Calculate"):
        area = calculate_area(side_length)
        st.write(f"The area of the square is: {area} square units")

if __name__ == "__main__":
    main()
