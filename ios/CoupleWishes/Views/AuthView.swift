import SwiftUI

struct AuthView: View {
    @Bindable var viewModel: AuthViewModel
    let onSuccess: () -> Void

    var body: some View {
        ScrollView {
            VStack(spacing: 32) {
                header

                VStack(spacing: 20) {
                    Picker("Mode", selection: $viewModel.isRegisterMode) {
                        Text("Register").tag(true)
                        Text("Login").tag(false)
                    }
                    .pickerStyle(.segmented)

                    if viewModel.isRegisterMode {
                        registerForm
                    } else {
                        loginForm
                    }

                    if let error = viewModel.errorMessage {
                        Text(error)
                            .font(.subheadline)
                            .foregroundStyle(.red)
                            .multilineTextAlignment(.center)
                    }

                    Button(action: submit) {
                        if viewModel.isLoading {
                            ProgressView()
                                .tint(.white)
                        } else {
                            Text(viewModel.isRegisterMode ? "Create Account" : "Sign In")
                        }
                    }
                    .buttonStyle(PrimaryButtonStyle(isDisabled: !viewModel.isFormValid || viewModel.isLoading))
                    .disabled(!viewModel.isFormValid || viewModel.isLoading)
                }
                .cardStyle()
            }
            .padding(24)
        }
        .background(AppTheme.background)
    }

    private var header: some View {
        VStack(spacing: 12) {
            Image(systemName: "heart.circle.fill")
                .font(.system(size: 72))
                .foregroundStyle(AppTheme.gradient)
                .symbolEffect(.pulse)

            Text("Couple Wishes")
                .font(.largeTitle.bold())

            Text("Share your dreams together")
                .font(.subheadline)
                .foregroundStyle(AppTheme.secondaryText)
        }
        .padding(.top, 40)
    }

    private var registerForm: some View {
        VStack(spacing: 16) {
            FormField(title: "Username", placeholder: "min. 3 characters") {
                TextField("Username", text: $viewModel.username)
                    .textContentType(.username)
                    .autocorrectionDisabled()
            }

            FormField(title: "Password", placeholder: "min. 8 characters") {
                SecureField("Password", text: $viewModel.password)
                    .textContentType(.newPassword)
            }
        }
    }

    private var loginForm: some View {
        FormField(title: "User ID", placeholder: "Your account ID") {
            TextField("User ID", text: $viewModel.userIdText)
                .keyboardType(.numberPad)
        }
    }

    private func submit() {
        Task {
            let success: Bool
            if viewModel.isRegisterMode {
                success = await viewModel.register()
            } else {
                success = await viewModel.login()
            }
            if success { onSuccess() }
        }
    }
}

struct FormField<Content: View>: View {
    let title: String
    let placeholder: String
    @ViewBuilder let content: Content

    var body: some View {
        VStack(alignment: .leading, spacing: 8) {
            Text(title)
                .font(.subheadline.weight(.medium))
                .foregroundStyle(AppTheme.secondaryText)
            content
                .padding(14)
                .background(Color(.systemGray6))
                .clipShape(RoundedRectangle(cornerRadius: 12))
        }
    }
}

#Preview {
    AuthView(viewModel: AuthViewModel(), onSuccess: {})
}
