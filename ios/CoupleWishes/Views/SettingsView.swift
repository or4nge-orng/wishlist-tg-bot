import SwiftUI

struct SettingsView: View {
    @Bindable var coupleViewModel: CoupleViewModel
    @Environment(\.dismiss) private var dismiss

    @State private var baseURL: String = SessionManager.shared.baseURL
    @State private var showLeaveConfirm = false
    @State private var showLogoutConfirm = false

    var body: some View {
        NavigationStack {
            Form {
                Section("Account") {
                    if let userId = SessionManager.shared.currentUserId {
                        LabeledContent("User ID", value: "\(userId)")
                    }
                    if let username = SessionManager.shared.currentUsername {
                        LabeledContent("Username", value: username)
                    }
                    if let coupleId = SessionManager.shared.currentCoupleId {
                        LabeledContent("Couple ID", value: "\(coupleId)")
                    }
                }

                Section("Server") {
                    TextField("API Base URL", text: $baseURL)
                        .textInputAutocapitalization(.never)
                        .autocorrectionDisabled()
                        .keyboardType(.URL)
                    Text("Default: http://127.0.0.1:8000")
                        .font(.caption)
                        .foregroundStyle(.secondary)
                }

                Section("Couple") {
                    Button("Leave Couple", role: .destructive) {
                        showLeaveConfirm = true
                    }
                }

                Section {
                    Button("Sign Out", role: .destructive) {
                        showLogoutConfirm = true
                    }
                }
            }
            .navigationTitle("Settings")
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .confirmationAction) {
                    Button("Done") {
                        SessionManager.shared.baseURL = baseURL
                        dismiss()
                    }
                }
            }
            .confirmationDialog("Leave this couple?", isPresented: $showLeaveConfirm, titleVisibility: .visible) {
                Button("Leave", role: .destructive) {
                    Task {
                        if await coupleViewModel.leaveCouple() {
                            dismiss()
                        }
                    }
                }
            }
            .confirmationDialog("Sign out?", isPresented: $showLogoutConfirm, titleVisibility: .visible) {
                Button("Sign Out", role: .destructive) {
                    SessionManager.shared.logout()
                    dismiss()
                }
            }
        }
    }
}

#Preview {
    SettingsView(coupleViewModel: CoupleViewModel())
}
