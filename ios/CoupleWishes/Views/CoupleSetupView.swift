import SwiftUI

struct CoupleSetupView: View {
    @Bindable var viewModel: CoupleViewModel
    let onComplete: () -> Void

    @State private var mode: SetupMode = .create

    enum SetupMode: String, CaseIterable {
        case create = "Create"
        case join = "Join"
    }

    var body: some View {
        ScrollView {
            VStack(spacing: 24) {
                VStack(spacing: 8) {
                    Image(systemName: "person.2.circle.fill")
                        .font(.system(size: 56))
                        .foregroundStyle(AppTheme.gradient)

                    Text("Find Your Partner")
                        .font(.title2.bold())

                    Text("Create a couple or join your partner's wishlist")
                        .font(.subheadline)
                        .foregroundStyle(AppTheme.secondaryText)
                        .multilineTextAlignment(.center)
                }
                .padding(.top, 20)

                if let userId = SessionManager.shared.currentUserId {
                    HStack {
                        Image(systemName: "person.fill")
                        Text("Your ID: \(userId)")
                            .font(.subheadline.weight(.semibold))
                        Spacer()
                        Button {
                            UIPasteboard.general.string = "\(userId)"
                        } label: {
                            Image(systemName: "doc.on.doc")
                                .foregroundStyle(AppTheme.accent)
                        }
                    }
                    .cardStyle()
                }

                Picker("Mode", selection: $mode) {
                    ForEach(SetupMode.allCases, id: \.self) { mode in
                        Text(mode.rawValue).tag(mode)
                    }
                }
                .pickerStyle(.segmented)

                if mode == .create {
                    createSection
                } else {
                    joinSection
                }

                if let error = viewModel.errorMessage {
                    Text(error)
                        .font(.subheadline)
                        .foregroundStyle(.red)
                        .multilineTextAlignment(.center)
                }

                if let success = viewModel.successMessage {
                    Text(success)
                        .font(.subheadline)
                        .foregroundStyle(.green)
                        .multilineTextAlignment(.center)
                }
            }
            .padding(24)
        }
        .background(AppTheme.background)
    }

    private var createSection: some View {
        VStack(spacing: 16) {
            FormField(title: "Partner's User ID", placeholder: "Optional — add later") {
                TextField("Partner ID", text: $viewModel.partnerIdText)
                    .keyboardType(.numberPad)
            }

            Button {
                Task {
                    let success: Bool
                    if viewModel.partnerIdText.isEmpty {
                        success = await viewModel.createSoloCouple()
                    } else {
                        success = await viewModel.createCoupleWithPartner()
                    }
                    if success { onComplete() }
                }
            } label: {
                if viewModel.isLoading {
                    ProgressView().tint(.white)
                } else {
                    Text(viewModel.partnerIdText.isEmpty ? "Start Solo Wishlist" : "Create Couple")
                }
            }
            .buttonStyle(PrimaryButtonStyle(isDisabled: viewModel.isLoading))
            .disabled(viewModel.isLoading)

            Text("Start solo and invite your partner later, or enter their ID now.")
                .font(.caption)
                .foregroundStyle(AppTheme.secondaryText)
                .multilineTextAlignment(.center)
        }
        .cardStyle()
    }

    private var joinSection: some View {
        VStack(spacing: 16) {
            FormField(title: "Partner's User ID", placeholder: "Required") {
                TextField("Partner ID", text: $viewModel.partnerIdText)
                    .keyboardType(.numberPad)
            }

            Button {
                Task {
                    if await viewModel.joinExistingCouple() {
                        onComplete()
                    }
                }
            } label: {
                if viewModel.isLoading {
                    ProgressView().tint(.white)
                } else {
                    Text("Join Partner")
                }
            }
            .buttonStyle(PrimaryButtonStyle(isDisabled: viewModel.partnerIdText.isEmpty || viewModel.isLoading))
            .disabled(viewModel.partnerIdText.isEmpty || viewModel.isLoading)

            Text("Your partner must already have a couple created.")
                .font(.caption)
                .foregroundStyle(AppTheme.secondaryText)
                .multilineTextAlignment(.center)
        }
        .cardStyle()
    }
}

#Preview {
    CoupleSetupView(viewModel: CoupleViewModel(), onComplete: {})
}
