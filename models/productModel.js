import mongoose from "mongoose";

const productSchema = new mongoose.Schema(
  {
    name: {
      type: String,
      required: true,
    },
    slug: {
      type: String,
      required: true,
    },
    description: {
      type: String,
      required: true,
    },
    price: {
      type: Number,
      required: true,
    },
    category: {
      type: mongoose.ObjectId,
      ref: "Category",
      required: true,
    },
    quantity: {
      type: Number,
      required: true,
    },
    photo: {
      data: Buffer,
      contentType: String,
    },
    shipping: {
      type: Boolean,
    },
    size: {
      type: String,
      enum: ['XXS', 'XS', 'S', 'M', 'L', 'XL', 'XXL'],
      required: true,
    },
    theme: {
      type: String,
      enum: ['summer', 'winter', 'autumn', 'spring'],
      required: true,
    },
    predictedPrice: {
      type: Number,
      default: null, 
    },
  },
  { timestamps: true }
);

export default mongoose.model("Products", productSchema);
