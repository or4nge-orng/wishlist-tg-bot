import SwiftUI

struct WishFormView: View {
    enum Mode {
        case create
        case edit(Wish)

        var title: String {
            switch self {
            case .create: return "New Wish"
            case .edit: return "Edit Wish"
            }
        }

        var buttonTitle: String {
            switch self {
            case .create: return "Add Wish"
            case .edit: return "Save Changes"
            }
        }
    }

    let mode: Mode
    @Bindable var viewModel: WishlistViewModel
    @Environment(\.dismiss) private var dismiss

    @State private var name = ""
    @State private var priceText = ""
    @State private var url = ""
    @State private var articleText = ""
    @State private var imageURL = ""
    @State private var isSaving = false
    @State private var errorMessage: String?

    private var isValid: Bool {
        !name.trimmingCharacters(in: .whitespaces).isEmpty &&
        Double(priceText.replacingOccurrences(of: ",", with: ".")) != nil
    }

    var body: some View {
        NavigationStack {
            ScrollView {
                VStack(spacing: 20) {
                    FormField(title: "Name", placeholder: "What do you wish for?") {
                        TextField("Wish name", text: $name)
                    }

                    FormField(title: "Price", placeholder: "0") {
                        TextField("Price", text: $priceText)
                            .keyboardType(.decimalPad)
                    }

                    FormField(title: "Product URL", placeholder: "Optional") {
                        TextField("https://...", text: $url)
                            .keyboardType(.URL)
                            .textInputAutocapitalization(.never)
                            .autocorrectionDisabled()
                    }

                    FormField(title: "Article / SKU", placeholder: "Optional") {
                        TextField("Article number", text: $articleText)
                            .keyboardType(.numberPad)
                    }

                    if case .edit = mode {
                        FormField(title: "Image URL", placeholder: "Optional") {
                            TextField("https://...", text: $imageURL)
                                .keyboardType(.URL)
                                .textInputAutocapitalization(.never)
                                .autocorrectionDisabled()
                        }
                    }

                    if let errorMessage {
                        Text(errorMessage)
                            .font(.subheadline)
                            .foregroundStyle(.red)
                    }

                    Button(action: save) {
                        if isSaving {
                            ProgressView().tint(.white)
                        } else {
                            Text(mode.buttonTitle)
                        }
                    }
                    .buttonStyle(PrimaryButtonStyle(isDisabled: !isValid || isSaving))
                    .disabled(!isValid || isSaving)
                }
                .padding(24)
            }
            .background(AppTheme.background)
            .navigationTitle(mode.title)
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .cancellationAction) {
                    Button("Cancel") { dismiss() }
                }
            }
            .onAppear(perform: populateFields)
        }
    }

    private func populateFields() {
        if case .edit(let wish) = mode {
            name = wish.name
            priceText = wish.price == floor(wish.price)
                ? String(Int(wish.price))
                : String(wish.price)
            url = wish.url
            articleText = wish.article > 0 ? String(wish.article) : ""
            imageURL = wish.image ?? ""
        }
    }

    private func save() {
        guard let price = Double(priceText.replacingOccurrences(of: ",", with: ".")) else { return }
        let article = Int(articleText) ?? 0

        isSaving = true
        errorMessage = nil

        Task {
            let success: Bool
            switch mode {
            case .create:
                success = await viewModel.createWish(
                    name: name.trimmingCharacters(in: .whitespaces),
                    price: price,
                    url: url,
                    article: article
                )
            case .edit(let wish):
                success = await viewModel.updateWish(
                    wish,
                    name: name.trimmingCharacters(in: .whitespaces),
                    price: price,
                    url: url,
                    article: article,
                    image: imageURL
                )
            }

            isSaving = false
            if success {
                dismiss()
            } else {
                errorMessage = viewModel.errorMessage
            }
        }
    }
}

#Preview {
    WishFormView(mode: .create, viewModel: WishlistViewModel())
}
