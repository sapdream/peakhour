def main():
  st.title('Clinic Peak Hour Prediction System')
  input_text = st.date_input("Enter Date to find busyness")

  results = getprediction(input_text)
  st.markdown(results)

if __name__ == "__main__":
    main()
